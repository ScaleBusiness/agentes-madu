"""Mostra a transcrição com pausas e sugere velocidade e limiar de silêncio.
Uso: python3 analisar.py video.mp4 palavras.json
"""
import json, re, subprocess, sys

ALVO_PPM = 170       # ritmo-alvo (palavras por minuto, sem pausas)
VEL_MAX = 1.25

video, palavras = sys.argv[1], json.load(open(sys.argv[2]))

linhas, linha, gaps, gaptot = [], f"[{palavras[0]['s']:.2f}] ", 0, 0.0
for k, w in enumerate(palavras):
    if k:
        g = w["s"] - palavras[k - 1]["e"]
        if g >= 0.35:
            gaps += 1
            gaptot += g
            linhas.append(linha + f" <{g:.1f}s>")
            linha = f"[{w['s']:.2f}] "
    linha += f"{w['w']} "
linhas.append(linha)
print("\n".join(linhas))

fala = palavras[-1]["e"] - palavras[0]["s"] - gaptot
ppm = len(palavras) / (fala / 60)
vel = min(max(ALVO_PPM / ppm, 1.0), VEL_MAX)
vel = round(round(vel / 0.05) * 0.05, 2)

r = subprocess.run(["ffmpeg", "-hide_banner", "-i", video, "-vn", "-af", "volumedetect", "-f", "null", "-"],
                   capture_output=True, text=True).stderr
media = float(re.search(r"mean_volume: (-?[\d.]+)", r).group(1))
limiar = int(round(min(max(media - 3, -40), -30)))

suspeitas = [(w["w"], w["s"]) for w in palavras
             if (w["e"] - w["s"]) > 0.15 + 0.1 * max(sum(c.isalpha() for c in w["w"]), 1)]

print("---")
print(json.dumps({
    "duracao_fala": round(palavras[-1]["e"], 1),
    "palavras": len(palavras),
    "pausas_longas": gaps, "tempo_em_pausa": round(gaptot, 1),
    "ritmo_sem_pausas_ppm": round(ppm),
    "velocidade_sugerida": vel,
    "volume_medio_db": media,
    "silencio_db_sugerido": limiar,
    "palavras_com_pausa_engolida": suspeitas[:15],
}, ensure_ascii=False, indent=1))
