"""Verify generated routes, SEO, original media retention and local references."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'_site'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.h1=0;self.canonical=False;self.desc=False;self.alt_errors=[];self.schemas=[];self.schema=False;self.buf=''
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if a.get('id'):assert a['id'] not in self.ids, 'Duplicate id '+a['id'];self.ids.add(a['id'])
  if t=='h1':self.h1+=1
  if t=='link' and a.get('rel')=='canonical':self.canonical=a.get('href','').startswith('https://fifty.ink/')
  if t=='meta' and a.get('name')=='description':self.desc=bool(a.get('content'))
  if t=='img' and 'alt' not in a:self.alt_errors.append(a.get('src'))
  for k in ['href','src','poster','data-src','data-mobile']:
   if a.get(k):self.refs.append(a[k])
  if a.get('srcset'):
   self.refs.extend(x.strip().split()[0] for x in a['srcset'].split(','))
  if t=='script' and a.get('type')=='application/ld+json':self.schema=True;self.buf=''
 def handle_data(self,d):
  if self.schema:self.buf+=d
 def handle_endtag(self,t):
  if t=='script' and self.schema:self.schemas.append(json.loads(self.buf));self.schema=False
pages={}
for p in SITE.rglob('*.html'):
 s=Page();s.feed(p.read_text());pages[p]=s
 assert s.h1==1, f'{p}: expected one h1, got {s.h1}'
 assert s.canonical and s.desc and s.schemas, f'{p}: missing SEO'
 assert not s.alt_errors, f'{p}: missing alt'
errors=[]
for p,s in pages.items():
 for ref in s.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=SITE/unquote(u.path.lstrip('/')) if u.path.startswith('/') else p.parent/unquote(u.path)
  if not u.path:target=p
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{p.relative_to(SITE)} -> {ref}')
  elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(f'{p.relative_to(SITE)} -> missing anchor {ref}')
assert not errors, '\n'.join(errors)
original=json.loads((ROOT/'source/media-audit.json').read_text())
assert all((SITE/a['path']).exists() for a in original['assets']), 'Original media missing'
assert all((SITE/m['path']).exists() for m in original['assembled_videos']), 'Assembled media missing'
assert 'editorial.css' in (SITE/'index.html').read_text() and '/style.css' not in (SITE/'index.html').read_text()
assert len(list((ROOT/'assets/photography').glob('*.jpg')))==(ROOT/'photography/index.html').read_text().count('data-photo '), 'Photo archive incomplete'
print(f'PASS: {len(pages)} HTML documents; all internal links, anchors, media and schema checked; all original media retained.')
