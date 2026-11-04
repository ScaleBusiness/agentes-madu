"""Cobre nomes e dados da família nas imagens (sigilo · Sarah 14/10). Uso: python3 anonimizar.py entrada saida"""
import sys, re, Vision
from Foundation import NSURL, NSMakeRange
from PIL import Image, ImageFilter
ALVO = re.compile(r'(laurinha|laura|carol|maria carolina|carolina|gabriel|dudu|\d+\s*meses)', re.I)
ent, sai = sys.argv[1], sys.argv[2]
im = Image.open(ent).convert('RGB'); W, H = im.size
req = Vision.VNRecognizeTextRequest.alloc().init(); req.setRecognitionLanguages_(['pt-BR']); req.setRecognitionLevel_(0)
h = Vision.VNImageRequestHandler.alloc().initWithURL_options_(NSURL.fileURLWithPath_(ent), None); h.performRequests_error_([req], None)
n = 0
for r in req.results() or []:
    cand = r.topCandidates_(1)[0]; t = cand.string()
    for m in ALVO.finditer(t):
        bb, err = cand.boundingBoxForRange_error_(NSMakeRange(m.start(), m.end() - m.start()), None)
        if bb is None: continue
        b = bb.boundingBox()
        x0 = int(b.origin.x * W) - 6; y1 = int(H - b.origin.y * H) + 6
        x1 = int((b.origin.x + b.size.width) * W) + 6; y0 = int(H - (b.origin.y + b.size.height) * H) - 6
        x0, y0, x1, y1 = max(0, x0), max(0, y0), min(W, x1), min(H, y1)
        reg = im.crop((x0, y0, x1, y1))
        reg = reg.resize((max(1, (x1 - x0) // 14), max(1, (y1 - y0) // 14)), Image.BILINEAR).resize((x1 - x0, y1 - y0), Image.NEAREST).filter(ImageFilter.GaussianBlur(6))
        im.paste(reg, (x0, y0)); n += 1
        print('coberto:', repr(m.group(0)), (x0, y0, x1, y1))
im.save(sai, quality=92)
print(n, 'trechos cobertos ->', sai)
