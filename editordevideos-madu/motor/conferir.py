"""Compara o texto esperado (blocos do plano) com a retranscrição do vídeo final.
Uso: python3 conferir.py plano.json palavras_originais.json legendas.json  (ou lista de palavras da saída)
"""
import json, sys, re, difflib

def norm(t):
    return re.sub(r"[^\wà-ú]", "", t.lower())

plano = json.load(open(sys.argv[1]))
orig = json.load(open(sys.argv[2]))
if isinstance(orig, dict):
    orig = orig["palavras"]
saida = json.load(open(sys.argv[3]))
if isinstance(saida, dict):
    saida = saida["palavras"]

esperado = []
for s, e in plano["blocos"]:
    esperado += [norm(w["w"]) for w in orig if w["s"] >= s - 0.05 and w["s"] < e - 0.02 and w["e"] <= e + 0.3]
obtido = [norm(w["w"]) for w in saida]

sm = difflib.SequenceMatcher(a=esperado, b=obtido, autojunk=False)
problemas = []
for op, a1, a2, b1, b2 in sm.get_opcodes():
    if op != "equal":
        ctx = " ".join(esperado[max(0, a1 - 3):a2 + 3])
        problemas.append(f"{op}: esperado '{' '.join(esperado[a1:a2])}' -> saiu '{' '.join(obtido[b1:b2])}'  | contexto: ...{ctx}...")
print(f"Semelhança: {sm.ratio():.1%} · {len(problemas)} diferenças")
for p in problemas:
    print(" -", p)
