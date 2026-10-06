The Dreamer — editorial cinematic website

Production: https://fifty.ink

Build editorial HTML and responsive image derivatives:
  python3 source/editorial.py
(Pillow required for image generation.)

Assemble all retained original media and validate:
  python3 scripts/assemble-media.py
  python3 scripts/verify-editorial.py
  node --check editorial.js

GitHub Pages deploys _site on main updates.
Design and audit: source/REDESIGN.md, source/media-audit.json.
Source credits: source/CONTENT_SOURCES.md.
Legacy generators and CSS are retained as historical source; production pages use editorial.css and editorial.js.
