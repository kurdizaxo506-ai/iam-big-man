#!/usr/bin/env python3
"""Run: python3 verify_project.py from extracted root."""
from pathlib import Path
import json,re,sys
from html.parser import HTMLParser
root=Path(__file__).resolve().parent
slugs="restaurant barber real-estate fitness beauty coffee hotel photography automotive dentist lawyer construction fashion travel education events pet-care tech bakery medical".split()
errors=[]
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.dupes=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:
   if a['id'] in self.ids:self.dupes.append(a['id'])
   self.ids.add(a['id'])
  for key in ('href','src'):
   if a.get(key):self.refs.append(a[key])
for slug in slugs:
 d=root/'templates'/slug
 for name in ('index.html','app.js','style.css','config.json','legal.html'):
  if not (d/name).is_file():errors.append(f'Missing {slug}/{name}')
 if not (root/'demos'/f'{slug}.html').exists():errors.append(f'Missing demo {slug}')
 try:
  cfg=json.loads((d/'config.json').read_text())
  html=(d/'index.html').read_text();m=re.search(r'<script id="ibm-embedded-config" type="application/json">(.*?)</script>',html,re.S)
  if not m or json.loads(m.group(1))!=cfg:errors.append(f'Config mismatch {slug}')
 except Exception as e:errors.append(f'JSON {slug}: {e}')
for path in root.rglob('*.html'):
 p=Parser();p.feed(path.read_text(errors='replace'))
 if p.dupes:errors.append(f'Duplicate ids in {path.relative_to(root)}: {p.dupes}')
 for ref in p.refs:
  if ref.startswith(('#','http:','https:','mailto:','tel:','data:','javascript:','//')) or ref.startswith('blob:'):continue
  dest=ref.split('#')[0].split('?')[0]
  if dest and not (path.parent/dest).exists():errors.append(f'Missing link {path.relative_to(root)} -> {dest}')
for slug in slugs:
 if not (root/'assets'/'photos'/f'{slug}.webp').exists():errors.append(f'Missing photo {slug}')
print(f'Checked {len(list(root.rglob("*.html")))} HTML files, {len(slugs)} templates, {len(slugs)} demos')
if errors:
 print('FAIL:',*errors,sep='\n - ');sys.exit(1)
print('PASS: files, relative links, embedded configs, unique HTML ids, photos')
