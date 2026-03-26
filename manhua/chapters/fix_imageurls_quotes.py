from pathlib import Path
import re

path = Path('chapter27_english.html')
text = path.read_text(encoding='utf-8')

m = re.search(r'(imageUrls\s*:\s*\[)(.*?)(\]\s*,)', text, flags=re.S)
if not m:
    raise SystemExit('imageUrls block not found')

prefix, body, suffix = m.group(1), m.group(2), m.group(3)
lines = [line.strip() for line in body.splitlines() if line.strip()]

clean = []
for line in lines:
    line = line.rstrip(',').strip()
    if not line:
        continue
    if not (line.startswith('"') or line.startswith("'")):
        line = '"' + line + '"'
    clean.append(line)

new_body = '\n            ' + ',\n            '.join(clean) + '\n        '

text = text[:m.start()] + prefix + new_body + suffix + text[m.end():]
path.write_text(text, encoding='utf-8')
print('done')
