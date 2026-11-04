import json, sys
from faster_whisper import WhisperModel
m = WhisperModel("medium", device="cpu", compute_type="int8")
segs, info = m.transcribe(sys.argv[1], language="pt", word_timestamps=True, vad_filter=False, beam_size=5)
words=[]
for s in segs:
    for w in s.words:
        words.append({"w":w.word.strip(),"s":round(w.start,3),"e":round(w.end,3),"p":round(w.probability,3)})
json.dump(words, open(sys.argv[2],"w"), ensure_ascii=False)
print(len(words),"palavras")
