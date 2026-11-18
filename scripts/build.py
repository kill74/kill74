#!/usr/bin/env python3
"""Gera banner, cabeçalho, cards e README do perfil.

Uso:  python scripts/build.py
Requer: pip install pillow numpy
Stars e datas vêm da API do GitHub (opcional: define GITHUB_TOKEN para evitar rate limit).
Sem rede, os cards mostram "-".
"""
import json
import os
import random
import textwrap
import urllib.request
from datetime import datetime
from html import escape
from pathlib import Path

import numpy as np
from PIL import Image

USER = "kill74"
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

# ---------- paleta e fontes ----------
BG, PANEL, CARD = "#0d1117", "#111820", "#0f141b"
BORDER, TEXT, MUTED, ACCENT = "#232b36", "#e6edf3", "#7d8590", "#ff8a1f"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

# ---------- conteúdo (edita aqui) ----------
PROJECTS = [
    dict(slug="teampulsebridge", repo="TeamPulseBridge", lang="Go",
         desc="Event ingestion bridge: Slack, Teams, GitHub and GitLab into one hardened pipeline. HMAC auth, OpenTelemetry, Terraform on GCP."),
    dict(slug="chatify", repo="Chatify", lang="Rust",
         desc="Self-hosted concurrent chat server. WebSocket, SQLite persistence, channels, DMs and file transfers."),
    dict(slug="cinderos", repo="CinderOS", lang="Shell",
         desc="Arch Linux ISO profile for a COSMIC workstation, aimed at AMD hardware for gaming and development."),
    dict(slug="pulsedata", repo="PulseData", lang="C#",
         desc="Full-stack ETL platform modelling e-commerce analytics, from ingestion to BI-ready output."),
    dict(slug="spo2sql", repo="SPO2SQL", lang="C#",
         desc="SharePoint Online to SQL Server sync via CSOM, with data quality routines before reporting."),
]
OSS = dict(slug="open-source", name="open-source", url="",
           desc="Contributing to Arch Linux's archinstall and the OpenCode AI coding agent. Fan of Omarchy.",
           cols=[("focus", "installers"), ("projects", "3"), ("status", "active")], right="contributor")

STACK = [
    ("systems", "Rust · Go · C · x86 Assembly"),
    ("backend", "C# · Python · Node.js · PHP · Bash · Lua"),
    ("frontend", "TypeScript · React · Next.js"),
    ("data", "PostgreSQL · SQLite · MongoDB · SQL Server · Oracle"),
    ("infra", "Docker · Terraform · Linux"),
]


# ---------- utilidades ----------
def rgb(h):
    return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], dtype=np.uint8)


def bayer(n):
    m = np.array([[0]])
    while m.shape[0] < n:
        m = np.block([[4 * m, 4 * m + 2], [4 * m + 3, 4 * m + 1]])
    return (m + 0.5) / (n * n)


def gh_info(repo):
    try:
        headers = {"User-Agent": "readme-build"}
        if os.environ.get("GITHUB_TOKEN"):
            headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
        req = urllib.request.Request(f"https://api.github.com/repos/{USER}/{repo}", headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            d = json.load(r)
        dt = datetime.fromisoformat(d["pushed_at"].replace("Z", "+00:00"))
        return str(d["stargazers_count"]), f"{dt:%b} {dt.day}"
    except Exception:
        return "-", "-"


def svg_wrap(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f"{body}</svg>")


def t(x, y, s, size=13, fill=TEXT, font=MONO, weight=400, anchor="start", ls=0):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{escape(s)}</text>')


# ---------- banner (PNG com dithering Bayer) ----------
def build_banner():
    W, H, S = 210, 52, 8
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    th = np.tile(bayer(8), (H // 8 + 1, W // 8 + 1))[:H, :W]

    # céu: brilho à volta de um sol baixo
    sx, sy = 150, 31
    glow = np.exp(-(((xx - sx) / 48) ** 2 + ((yy - sy) / 17) ** 2))
    lv = np.floor(glow * 3.2 + th - 0.1).clip(0, 3).astype(int)
    pal = np.array([rgb(BG), rgb("#3a1c0a"), rgb("#9a4a12"), rgb(ACCENT)])
    img = pal[lv]
    img[np.hypot(xx - sx, yy - sy) < 7] = rgb(ACCENT)

    # estrelas esparsas
    rnd = np.random.default_rng(74)
    stars = (rnd.random((H, W)) < 0.012) & (yy < 22)
    img[stars] = rgb("#3a4350")

    # três serras (longe -> perto)
    layers = [(33, 6, "#3a4350", "#1b222c", (0.09, 0.23, 0.51), (0.4, 2.1, 4.0)),
              (40, 5, "#2a323d", "#141a22", (0.07, 0.19, 0.43), (1.7, 0.3, 5.2)),
              (46, 4, "#1e252f", "#0a0e13", (0.11, 0.27, 0.6), (3.1, 4.4, 0.9))]
    for base, amp, edge, fill, freqs, phases in layers:
        h = base + sum(amp / (i + 1) * np.sin(xx * f + p) for i, (f, p) in enumerate(zip(freqs, phases)))
        mask = yy >= h
        v = np.clip(1 - (yy - h) / 14, 0, 1)
        col = np.where((v > th)[..., None], rgb(edge), rgb(fill))
        img = np.where(mask[..., None], col, img)

    Image.fromarray(img.astype(np.uint8)).resize((W * S, H * S), Image.NEAREST).save(
        ASSETS / "banner.png", optimize=True)


# ---------- cabeçalho ----------
def build_header():
    W, H = 900, 214
    b = [f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" fill="{BG}" stroke="{BORDER}"/>',
         f'<rect x="1" y="1" width="{W - 2}" height="33" fill="{PANEL}"/>',
         f'<line x1="0" y1="34.5" x2="{W}" y2="34.5" stroke="{BORDER}"/>',
         t(18, 22, "kill74@ipcb", 12, MUTED), t(103, 22, "~ $", 12, ACCENT), t(133, 22, "whoami", 12, TEXT),
         t(W - 18, 22, f"github.com/{USER}", 12, MUTED, anchor="end"),
         t(28, 104, "kill74", 60, TEXT, SANS, 700, ls=-2),
         t(30, 132, "Systems programmer and full-stack engineer.", 15, MUTED, SANS)]
    for i, (k, v) in enumerate([("now", "studying computer engineering, contributing to open source"),
                                ("next", "a 3D open-world RPG")]):
        y = 168 + i * 24
        b += [t(30, y, k, 11, MUTED), t(78, y, v, 13, TEXT)]
    gx, gy, cw, ch = 600, 35, 150, 89.5
    b.append(f'<line x1="{gx}.5" y1="35" x2="{gx}.5" y2="{H}" stroke="{BORDER}"/>')
    b.append(f'<line x1="{gx + cw}.5" y1="35" x2="{gx + cw}.5" y2="{H}" stroke="{BORDER}"/>')
    b.append(f'<line x1="{gx}" y1="{gy + ch}" x2="{W}" y2="{gy + ch}" stroke="{BORDER}"/>')
    cells = [("base", "Portugal"), ("status", "active"), ("focus", "systems + web"), ("stack", "Rust · Go · C#")]
    for i, (k, v) in enumerate(cells):
        cx, cy = gx + (i % 2) * cw + 16, gy + (i // 2) * ch
        b.append(t(cx, cy + 32, k, 11, MUTED))
        if k == "status":
            b.append(f'<rect x="{cx}" y="{cy + 47}" width="8" height="8" fill="{ACCENT}"/>')
            b.append(t(cx + 16, cy + 57, v, 13, TEXT, weight=700))
        else:
            b.append(t(cx, cy + 57, v, 13, TEXT, weight=700))
    (ASSETS / "header.svg").write_text(svg_wrap(W, H, "".join(b)), encoding="utf-8")


# ---------- cards ----------
def skyline(seed, x0, y0, w, h, cell=6):
    rnd = random.Random(seed)
    cols, rows = w // cell, h // cell
    bz = bayer(4)
    hs, v = [], rnd.random()
    for _ in range(cols):
        v = min(max(v + rnd.uniform(-.22, .22), .2), 1)
        hs.append(v)
    acc, dim = [], []
    for c in range(cols):
        top = hs[c] * rows
        for r in range(rows):
            if r >= top:
                break
            frac = r / top
            cx, cy = x0 + c * cell, y0 + (rows - 1 - r) * cell
            cell_d = f"M{cx} {cy}h{cell}v{cell}h-{cell}z"
            if top - r <= 2:
                acc.append(cell_d)
            elif bz[r % 4][c % 4] < 1 - frac * 0.9:
                dim.append(cell_d)
    return (f'<path d="{"".join(dim)}" fill="#2b3440"/>'
            f'<path d="{"".join(acc)}" fill="{ACCENT}"/>')


def build_card(slug, name, desc, cols, right):
    W, H = 440, 264
    lines = textwrap.wrap(desc, 50)
    assert len(lines) <= 3, f"{slug}: descrição demasiado longa"
    b = [f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" fill="{CARD}" stroke="{BORDER}"/>',
         f'<rect x="1" y="1" width="{W - 2}" height="29" fill="{PANEL}"/>',
         f'<line x1="0" y1="30.5" x2="{W}" y2="30.5" stroke="{BORDER}"/>',
         t(16, 20, name, 12, TEXT, weight=700), t(W - 16, 20, right, 11, MUTED, anchor="end"),
         skyline(slug, 16, 40, 408, 60),
         t(16, 134, name, 22, TEXT, SANS, 700, ls=-0.5)]
    for i, ln in enumerate(lines):
        b.append(t(16, 160 + i * 18, ln, 13, MUTED, SANS))
    fy = H - 56
    b.append(f'<line x1="0" y1="{fy}.5" x2="{W}" y2="{fy}.5" stroke="{BORDER}"/>')
    cw = W / 3
    for i, (k, v) in enumerate(cols):
        x = i * cw + 16
        if i:
            b.append(f'<line x1="{i * cw:.1f}" y1="{fy}" x2="{i * cw:.1f}" y2="{H}" stroke="{BORDER}"/>')
        b += [t(x, fy + 20, k, 11, MUTED), t(x, fy + 40, v, 13, TEXT, weight=700)]
    (ASSETS / f"card-{slug}.svg").write_text(svg_wrap(W, H, "".join(b)), encoding="utf-8")


# ---------- stack ----------
def build_stack():
    W, rh = 900, 40
    H = 8 + rh * len(STACK) + 8
    b = [f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" fill="{BG}" stroke="{BORDER}"/>']
    for i, (k, v) in enumerate(STACK):
        y = 8 + i * rh
        if i:
            b.append(f'<line x1="0" y1="{y}.5" x2="{W}" y2="{y}.5" stroke="{BORDER}"/>')
        b += [f'<rect x="20" y="{y + 16}" width="8" height="8" fill="{ACCENT}"/>',
              t(44, y + 25, k, 12, MUTED), t(170, y + 25, v, 14, TEXT)]
    (ASSETS / "stack.svg").write_text(svg_wrap(W, H, "".join(b)), encoding="utf-8")


# ---------- README ----------
def anchor_open(url):
    return f'<a href="{url}">' if url else '<a>'


def build_readme(cards):
    grid = "\n".join(
        f'{anchor_open(u)}<img src="assets/card-{s}.svg" alt="{a}" width="49%"></a>' for u, s, a in cards)
    md = f"""<img src="assets/banner.png" alt="" width="100%">
<img src="assets/header.svg" alt="kill74 - systems programmer and full-stack engineer" width="100%">

Systems programmer and full-stack engineer based in Portugal. Computer engineering student at [IPCB](https://www.ipcb.pt).

I work across the full stack, from bare-metal kernels and systems daemons up to REST APIs and production UIs. I care about software that is correct, observable and built to survive contact with production.

I love open source (●'◡'●)

### Work

<p>
{grid}
</p>

### Stack

<img src="assets/stack.svg" alt="Rust, Go, C, C#, Python, TypeScript, PostgreSQL, Docker, Terraform" width="100%">

### Say hi

[Portfolio](https://guilhermewebsitee.vercel.app) · [LinkedIn](https://www.linkedin.com/in/guilherme-sales-35a580299) · guilhermesales4563@gmail.com
"""
    (ROOT / "README.md").write_text(md, encoding="utf-8")


def main():
    build_banner()
    build_header()
    build_stack()
    cards = []
    for p in PROJECTS:
        stars, upd = gh_info(p["repo"])
        build_card(p["slug"], p["repo"], p["desc"],
                   [("language", p["lang"]), ("stars", stars), ("updated", upd)],
                   f"updated {upd}" if upd != "-" else "")
        cards.append((f"https://github.com/{USER}/{p['repo']}", p["slug"], p["repo"]))
    build_card(OSS["slug"], OSS["name"], OSS["desc"], OSS["cols"], OSS["right"])
    cards.append((OSS["url"], OSS["slug"], "Open source"))
    build_readme(cards)
    print("ok")


if __name__ == "__main__":
    main()
