"""Assemble the complete, unchanged Dreamer site for GitHub Pages."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
excluded = {".git", ".github", ".media-parts", "scripts", "source", "_site", ".gitignore", "README.txt"}
for item in ROOT.iterdir():
    if item.name in excluded:
        continue
    destination = OUTPUT / item.name
    if item.is_dir():
        shutil.copytree(item, destination)
    else:
        shutil.copy2(item, destination)
manifest = json.loads((ROOT / "scripts/media-manifest.json").read_text())
for media in manifest:
    destination = OUTPUT / media["path"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    checksum = hashlib.sha256()
    with destination.open("wb") as target:
        for part in media["parts"]:
            with (ROOT / part).open("rb") as source:
                while chunk := source.read(1024 * 1024):
                    target.write(chunk)
                    checksum.update(chunk)
    if checksum.hexdigest() != media["sha256"]:
        raise RuntimeError(f"Media checksum mismatch: {media['path']}")
print(f"Site assembled; {len(manifest)} full-quality videos verified.")
