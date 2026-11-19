"""Several memory files. Pick one as the active space.

A space is a directory under memory/spaces/<name>/. Each write copies
the current graph.json to graph.<n>.json before replacing it, so a bad
teaching pass can be rolled back.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPACES = ROOT / "spaces"
ACTIVE = ROOT / "active.txt"

def list_spaces() -> list[str]:
    if not SPACES.is_dir():
        return []
    return sorted(p.name for p in SPACES.iterdir() if p.is_dir())

def use(name: str) -> Path:
    d = SPACES / name
    d.mkdir(parents=True, exist_ok=True)
    g = d / "graph.json"
    if not g.exists():
        g.write_text(json.dumps({"nodes": [], "links": []}, indent=2))
    ACTIVE.write_text(name)
    return g

def active() -> Path:
    name = ACTIVE.read_text().strip() if ACTIVE.exists() else "default"
    return use(name)

def save(graph: dict) -> Path:
    g = active()
    n = 1
    while (g.parent / f"graph.{n}.json").exists():
        n += 1
    if g.exists() and g.stat().st_size:
        shutil.copy(g, g.parent / f"graph.{n}.json")
    g.write_text(json.dumps(graph, indent=2))
    return g

def versions(name: str | None = None) -> list[str]:
    d = SPACES / (name or active().parent.name)
    return sorted(p.name for p in d.glob("graph*.json"))

def restore(name: str, version: str) -> Path:
    src = SPACES / name / version
    dst = use(name)
    shutil.copy(src, dst)
    return dst
