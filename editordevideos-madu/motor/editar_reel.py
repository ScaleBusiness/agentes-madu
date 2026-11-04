"""Motor de edição de Reels: gancho na frente, respiros removidos, zoom alternado, aceleração, 1080x1920.

Uso: python3 editar_reel.py plano.json
plano.json = {
  "entrada": "video.mp4", "saida": "base.mp4",
  "palavras": "palavras.json",          # transcrição do ORIGINAL (transcrever.py) — protege palavras
  "blocos": [[ini, fim], ...],           # trechos na ORDEM de exibição (gancho primeiro)
  "zoom_blocos": [1.12, null],           # opcional: zoom fixo por bloco (null = alternado)
  "silencio_db": -35, "silencio_min": 0.25, "folga": 0.1,
  "velocidade": 1.1,
  "zoom": 1.10, "zoom_intervalo": 4.0    # zoom 1.0 = desliga
}
"""
import json, re, subprocess, sys, os, tempfile

def silencios(entrada, db, dmin):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", entrada, "-vn", "-af",
                        f"silencedetect=noise={db}dB:d={dmin}", "-f", "null", "-"],
                       capture_output=True, text=True)
    ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    return list(zip(ini, fim))

def palavra_plausivel(w):
    # Palavra "longa demais" = Whisper absorveu a pausa; nesse caso vale o silêncio detectado.
    letras = sum(c.isalpha() for c in w["w"])
    return (w["e"] - w["s"]) <= 0.15 + 0.1 * max(letras, 1)

def proteger(a2, b2, palavras, margem=0.06):
    for w in palavras:
        if not palavra_plausivel(w):
            continue
        if w["s"] < a2 < w["e"] + margem:
            a2 = w["e"] + margem
        if w["s"] - margem < b2 < w["e"]:
            b2 = w["s"] - margem
    return a2, b2

def recortar(bloco, sil, folga, palavras, minimo=0.12):
    s, e = bloco
    partes, cursor = [], s
    for a, b in sil:
        a2, b2 = proteger(a + folga, b - folga, palavras)
        if b2 <= a2 or b2 <= s or a2 >= e:
            continue
        if a2 > cursor:
            partes.append([cursor, min(a2, e)])
        cursor = max(cursor, b2)
    if cursor < e:
        partes.append([cursor, e])
    return [p for p in partes if p[1] - p[0] >= minimo]

def render_parte(entrada, a, b, z, saida):
    dur = b - a
    crop = f"crop=iw/{z}:ih/{z}:(iw-iw/{z})/2:(ih-ih/{z})*0.35," if z > 1.001 else ""
    vf = (f"{crop}scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
          "fps=30,setsar=1")
    f = min(0.012, dur / 4)
    af = f"aresample=48000,afade=t=in:d={f:.3f},afade=t=out:st={dur - f:.3f}:d={f:.3f}"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-i", entrada,
                    "-t", f"{dur:.3f}", "-vf", vf, "-af", af, "-c:v", "libx264",
                    "-preset", "veryfast", "-crf", "16", "-c:a", "pcm_s16le", "-ar", "48000",
                    "-ac", "2", saida], check=True)

def dividir_para_zoom(partes, palavras, intervalo):
    # Troca de zoom só em fim de frase/vírgula, no meio da pausa entre as palavras.
    pontos = [(w["e"] + palavras[k + 1]["s"]) / 2 for k, w in enumerate(palavras[:-1])
              if w["w"][-1:] in ".?!,;:"]
    out = []
    for a, b in partes:
        ini = a
        for c in pontos:
            if ini + intervalo <= c <= b - 1.0:
                out.append([ini, c])
                ini = c
        out.append([ini, b])
    return out

def main(plano_path):
    p = json.load(open(plano_path))
    sil = silencios(p["entrada"], p.get("silencio_db", -35), p.get("silencio_min", 0.25))
    palavras = json.load(open(p["palavras"])) if p.get("palavras") else []
    if isinstance(palavras, dict):
        palavras = palavras["palavras"]
    zmax, zint = p.get("zoom", 1.10), p.get("zoom_intervalo", 4.0)
    zfix = p.get("zoom_blocos", [])
    tmp = tempfile.mkdtemp()
    lista, relatorio, n = [], [], 0
    estado, desde = False, 0.0
    for i, bloco in enumerate(p["blocos"]):
        partes = recortar(bloco, sil, p.get("folga", 0.1), palavras)
        fixo = zfix[i] if i < len(zfix) else None
        pedacos = partes if (fixo is not None or zmax <= 1.001) else dividir_para_zoom(partes, palavras, zint)
        for a, b in pedacos:
            if fixo is not None:
                z = fixo
            else:
                if desde >= zint:
                    estado, desde = not estado, 0.0
                z = zmax if estado else 1.0
                desde += b - a
            f = os.path.join(tmp, f"p{n:04d}.mkv")
            render_parte(p["entrada"], a, b, z, f)
            lista.append(f)
            n += 1
        relatorio.append({"bloco": bloco, "trechos": len(partes),
                          "dur_original": round(bloco[1] - bloco[0], 2),
                          "dur_sem_respiro": round(sum(b - a for a, b in partes), 2)})
    lst = os.path.join(tmp, "lista.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{f}'\n" for f in lista)
    v = p.get("velocidade", 1.0)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-vf", f"setpts=PTS/{v},fps=30", "-af",
                    f"atempo={v},loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", p["saida"]],
                   check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                                "-of", "csv=p=0", p["saida"]], capture_output=True, text=True).stdout)
    print(json.dumps({"blocos": relatorio, "partes": n, "velocidade": v,
                      "duracao_final": round(dur, 2)}, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1])
