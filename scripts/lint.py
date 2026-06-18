#!/usr/bin/env python3
"""Lint du repo marketing-skills.

Vérifie ce qui garantit la qualité et la cohérence du repo :
  1. Frontmatter des SKILL.md (name = nom du dossier, description présente).
  2. Pas de tiret cadratin « — » en prose (la règle que le repo lui-même enseigne).
  3. Tous les liens markdown internes (.md) résolvent.
  4. Manifestes de plugin (.claude-plugin/*.json) valides.

Sort en erreur (code 1) si une règle est violée. Aucune dépendance externe.
Usage : python3 scripts/lint.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def rel(p):
    return p.relative_to(ROOT)


def err(msg):
    errors.append(msg)


# 1. Frontmatter des SKILL.md
for skill in sorted(ROOT.glob("skills/*/SKILL.md")):
    text = skill.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{rel(skill)} : frontmatter YAML manquant en tête de fichier")
        continue
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    dirname = skill.parent.name
    if fm.get("name") != dirname:
        err(f"{rel(skill)} : 'name' ({fm.get('name')!r}) doit valoir le nom du dossier ({dirname!r})")
    desc = fm.get("description", "")
    if not desc:
        err(f"{rel(skill)} : 'description' manquante (c'est elle qui déclenche le skill)")
    elif len(desc) > 1024:
        err(f"{rel(skill)} : 'description' trop longue ({len(desc)} car., max 1024)")


# 2 & 3. Em-dash en prose + liens .md, sur tous les markdown du repo
md_files = (
    list(ROOT.glob("skills/**/*.md"))
    + list(ROOT.glob("docs/**/*.md"))
    + list((ROOT / ".github").glob("**/*.md"))
    + [ROOT / "README.md"]
)
for md in md_files:
    if not md.exists():
        continue
    lines = md.read_text(encoding="utf-8").split("\n")
    in_code = False
    in_fm = False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if i == 1 and s == "---":
            in_fm = True
            continue
        if in_fm:
            if s == "---":
                in_fm = False
            continue
        # Tiret cadratin utilisé comme ponctuation de prose (espace-cadratin-espace),
        # hors lignes de titre. Les mentions « (—) » ou « `—` » ne matchent pas.
        if not s.startswith("#") and " — " in line:
            err(f"{rel(md)}:{i} : tiret cadratin « — » en prose (remplacer par : ; . , ou parenthèses)")

    for mlink in re.finditer(r"\]\(([^)#]+\.md)(?:#[^)]*)?\)", md.read_text(encoding="utf-8")):
        link = mlink.group(1)
        if link.startswith(("http://", "https://")):
            continue
        if not (md.parent / link).resolve().exists():
            err(f"{rel(md)} : lien interne cassé -> {link}")


# 4. Manifestes de plugin
for jf, required in [
    (".claude-plugin/plugin.json", ("name", "description")),
    (".claude-plugin/marketplace.json", ("name", "plugins")),
]:
    p = ROOT / jf
    if not p.exists():
        err(f"{jf} : absent")
        continue
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"{jf} : JSON invalide ({e})")
        continue
    for k in required:
        if not data.get(k):
            err(f"{jf} : champ '{k}' manquant")
    if jf.endswith("marketplace.json") and not isinstance(data.get("plugins"), list):
        err(f"{jf} : 'plugins' doit être une liste")


if errors:
    print(f"❌ Lint échoué ({len(errors)}) :")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("✅ Lint OK")
