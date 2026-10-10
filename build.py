from pathlib import Path
import re,base64
root=Path(__file__).resolve().parent
p=root/'src/gpu-dive.template.js'
s=p.read_text()
data='data:image/png;base64,'+base64.b64encode((root/'assets/card.png').read_bytes()).decode()
js=s.replace('__CARD_DATA__',data)
(root/'gpu-dive.js').write_text(js)
html='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>GPU Dive · RTX 4070</title><meta name="description" content="Click through a graphics card, its chip, SMs and execution hierarchy."><style>html,body{margin:0;width:100%;height:100%;background:#090d10}gpu-dive{height:100dvh;width:100%;display:block}</style></head><body><gpu-dive></gpu-dive><script>'''+js+'''</script></body></html>'''
(root/'index.html').write_text(html)
(root/'embed.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>GPU Dive embed example</title><style>body{margin:0;padding:32px;background:#f4f4ef;font-family:system-ui}main{max-width:1100px;margin:auto}gpu-dive{display:block;height:700px;border-radius:20px;overflow:hidden}h1{font-size:20px;font-weight:500}</style></head><body><main><h1>A small GPU, a lot to explore.</h1><gpu-dive></gpu-dive></main><script src="gpu-dive.js"></script></body></html>''')
print('Built independent HTML and embeddable component',len(js),'bytes')
