#!/usr/bin/env python3
"""Generate infographic images for blog posts. Pillow-based, dark theme."""

import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "public", "images", "posts", "claude-code-runs-my-life")
os.makedirs(OUT, exist_ok=True)

# Fonts
MONO = "/System/Library/Fonts/SFNSMono.ttf"
SANS = "/System/Library/Fonts/SFNS.ttf"
MENLO = "/System/Library/Fonts/Menlo.ttc"

# Dark theme colors (matching blog dark mode)
BG = "#212737"
FG = "#eaedf3"
ACCENT = "#ff6b01"
MUTED = "#8b95b0"
BORDER = "#ab4b08"
CARD_BG = "#2a3148"
SUCCESS = "#4ade80"
DANGER = "#f87171"

# Subtle gradient helper
def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def font(path, size):
    return ImageFont.truetype(path, size)


def new_canvas(w, h):
    img = Image.new("RGB", (w, h), BG)
    return img, ImageDraw.Draw(img)


def save(img, name):
    path = os.path.join(OUT, name)
    img.save(path, quality=95)
    print(f"  -> {path}")


def draw_rounded_rect(d, xy, radius, fill=None, outline=None, width=1):
    """Draw rounded rectangle with proper fill."""
    d.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


# ─── Image 1: Stats Hero (improved) ────────────────────────────────

def generate_stats_hero():
    """Big numbers card — cleaner layout, better rhythm."""
    W, H = 1200, 600
    img, d = new_canvas(W, H)

    # Subtle top accent line
    d.rectangle([(0, 0), (W, 4)], fill=ACCENT)

    # Title
    d.text((60, 28), "THE SETUP", font=font(MONO, 14), fill=MUTED)

    stats = [
        ("13", "projects"),
        ("68", "skills"),
        ("29", "agents"),
        ("14", "hooks"),
    ]

    # 4 columns — top row with big numbers
    col_w = (W - 120) // 4
    for i, (num, label) in enumerate(stats):
        x = 60 + i * col_w
        cx = x + col_w // 2 - 40  # center-ish

        # Number
        f_num = font(SANS, 110)
        d.text((cx, 70), num, font=f_num, fill=ACCENT)
        # Label
        d.text((cx + 2, 195), label, font=font(SANS, 24), fill=FG)

    # Subtle divider
    d.line([(60, 250), (W - 60, 250)], fill=BORDER, width=1)

    # Bottom row — secondary stats in cards
    bottom_stats = [
        ("6", "MCP servers"),
        ("26", "memory files"),
        ("~400", "lines in CLAUDE.md"),
    ]
    card_w = (W - 160) // 3
    for i, (num, label) in enumerate(bottom_stats):
        x = 60 + i * (card_w + 20)
        # Card background
        draw_rounded_rect(d, [(x, 275), (x + card_w, 375)], radius=8, fill=CARD_BG)
        # Number
        d.text((x + 20, 285), num, font=font(SANS, 44), fill=FG)
        # Label
        d.text((x + 20, 340), label, font=font(SANS, 16), fill=MUTED)

    # Footer tagline
    d.text((60, H - 55), "1 human", font=font(MONO, 20), fill=ACCENT)
    d.text((210, H - 55), "·", font=font(MONO, 20), fill=MUTED)
    d.text((240, H - 55), "0 regrets", font=font(MONO, 20), fill=ACCENT)

    # Subtle bottom accent
    d.rectangle([(0, H - 4), (W, H)], fill=ACCENT)

    save(img, "stats-hero.png")


# ─── Image 2: 6 Layers Stack (improved) ────────────────────────────

def generate_layers():
    """Visual stack of 6 layers — tighter, more visual distinction."""
    W, H = 1200, 680
    img, d = new_canvas(W, H)

    # Top accent
    d.rectangle([(0, 0), (W, 4)], fill=ACCENT)

    d.text((60, 24), "THE 6 LAYERS", font=font(MONO, 14), fill=MUTED)

    layers = [
        ("6", "AUTONOMOUS TEAM", "Agents run on cron, no human in the loop", ACCENT, "launchd + SQLite + 10 agents"),
        ("5", "MEMORY", "4 layers with strict routing rules", "#a78bfa", "CLAUDE.md / auto / MCP / KB"),
        ("4", "HOOKS", "14 event handlers across 10 types", "#60a5fa", "PreToolUse / PostToolUse / Stop"),
        ("3", "AGENTS", "29 specialized personalities", "#4ade80", "carousel-writer / telegram / photo-curator"),
        ("2", "SKILLS", "68 slash commands for everything", "#fbbf24", "/status / /notify / /digest / /inbox"),
        ("1", "FOUNDATION", "CLAUDE.md — 400 lines of who I am", "#f87171", "rules + conventions + guardrails"),
    ]

    y_start = 60
    row_h = 85
    gap = 10
    bar_x = 60
    bar_w = W - 120

    for i, (num, title, desc, color, detail) in enumerate(layers):
        y = y_start + i * (row_h + gap)

        # Pyramid indent
        indent = i * 12
        x1 = bar_x + indent
        x2 = bar_x + bar_w - indent

        # Background bar
        draw_rounded_rect(d, [(x1, y), (x2, y + row_h)], radius=10, fill=CARD_BG)

        # Left accent stripe
        d.rounded_rectangle([(x1, y), (x1 + 5, y + row_h)], radius=3, fill=color)

        # Layer badge
        badge_w = 42
        draw_rounded_rect(d, [(x1 + 18, y + 12), (x1 + 18 + badge_w, y + 38)], radius=4, fill=color + "30")
        d.text((x1 + 24, y + 13), f"L{num}", font=font(MONO, 16), fill=color)

        # Title
        d.text((x1 + 72, y + 12), title, font=font(SANS, 22), fill=FG)

        # Description
        d.text((x1 + 72, y + 42), desc, font=font(SANS, 15), fill=MUTED)

        # Detail tag (right side)
        d.text((x2 - 280, y + 42), detail, font=font(MONO, 12), fill=color + "80")

    # Bottom accent
    d.rectangle([(0, H - 4), (W, H)], fill=ACCENT)

    save(img, "six-layers.png")


# ─── Image 3: Before / After (improved) ────────────────────────────

def generate_before_after():
    """Two-column comparison — better markers, visual weight."""
    W, H = 1200, 630
    img, d = new_canvas(W, H)

    mid = W // 2

    # Top accent
    d.rectangle([(0, 0), (W, 4)], fill=ACCENT)

    # Left column — Before (darker bg)
    d.rectangle([(0, 4), (mid - 1, H)], fill="#181d2a")

    # "BEFORE" header with red underline
    d.text((50, 32), "BEFORE", font=font(SANS, 22), fill=DANGER)
    d.line([(50, 62), (160, 62)], fill=DANGER, width=2)

    before = [
        "Context lost every session",
        "Manual deploys, manual checks",
        "Same debugging 3x/week",
        "10 min switching between projects",
        "Forget what I did yesterday",
        '"Wait, which photos did I use?"',
        "Ideas lost in random notes",
    ]

    for i, text in enumerate(before):
        y = 90 + i * 70
        # Red circle with X
        cx, cy = 55, y + 10
        d.ellipse([(cx, cy), (cx + 22, cy + 22)], fill=DANGER + "25", outline=DANGER)
        d.text((cx + 5, cy + 1), "x", font=font(MONO, 16), fill=DANGER)
        d.text((90, y + 7), text, font=font(SANS, 18), fill="#9ca3af")

    # Right column — After
    # "AFTER" header with green underline
    d.text((mid + 50, 32), "AFTER", font=font(SANS, 22), fill=SUCCESS)
    d.line([(mid + 50, 62), (mid + 140, 62)], fill=SUCCESS, width=2)

    after = [
        "Memory persists across sessions",
        "One-command deploy + auto-checks",
        "Solutions saved, never re-debugged",
        "/status shows all 13 projects in 2s",
        "/digest: full changelog on wakeup",
        "Photo curator tracks every image",
        "/inbox pulls ideas from all sources",
    ]

    for i, text in enumerate(after):
        y = 90 + i * 70
        # Green circle with checkmark
        cx, cy = mid + 55, y + 10
        d.ellipse([(cx, cy), (cx + 22, cy + 22)], fill=SUCCESS + "25", outline=SUCCESS)
        d.text((cx + 4, cy - 1), "+", font=font(MONO, 18), fill=SUCCESS)
        d.text((mid + 90, y + 7), text, font=font(SANS, 18), fill=FG)

    # Center divider — dashed feel
    for y in range(20, H - 20, 8):
        d.line([(mid, y), (mid, y + 4)], fill=BORDER, width=1)

    # Bottom accent
    d.rectangle([(0, H - 4), (W, H)], fill=ACCENT)

    save(img, "before-after.png")


# ─── Image 4: Terminal Statusline (improved) ───────────────────────

def generate_terminal():
    """Terminal mockup — brighter annotations."""
    W, H = 1200, 420
    img, d = new_canvas(W, H)

    # Terminal window
    term_x, term_y = 30, 20
    term_w, term_h = W - 60, H - 40
    draw_rounded_rect(d, [(term_x, term_y), (term_x + term_w, term_y + term_h)],
                      radius=12, fill="#0d1117")

    # Title bar
    draw_rounded_rect(d, [(term_x, term_y), (term_x + term_w, term_y + 40)],
                      radius=12, fill="#161b22")
    d.rectangle([(term_x, term_y + 28), (term_x + term_w, term_y + 40)], fill="#161b22")

    # Traffic lights
    for i, color in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        d.ellipse([(55 + i * 22, 30), (55 + i * 22 + 14, 44)], fill=color)

    # Terminal title
    d.text((W // 2 - 60, 30), "claude-code", font=font(MONO, 14), fill=MUTED)

    # Command prompt
    y = 80
    d.text((60, y), "~/dev/kairos-press", font=font(MENLO, 16), fill="#58a6ff")
    d.text((265, y), "main", font=font(MENLO, 16), fill="#3fb950")
    d.text((320, y), "$", font=font(MENLO, 16), fill=MUTED)

    # Statusline — the star of the show
    y = 130
    parts = [
        ("[73K/200K]", "#3fb950", 60),
        (" · ", MUTED, 215),
        ("$0.84", FG, 250),
        (" · ", MUTED, 350),
        ("[5h 23%", "#fbbf24", 385),
        (" · ", MUTED, 515),
        ("7d 41%]", "#fb923c", 550),
        (" · ", MUTED, 690),
        ("15:30 -> 15:31", MUTED + "cc", 725),
    ]
    for text, color, x in parts:
        d.text((x, y), text, font=font(MENLO, 22), fill=color)

    # Annotation arrows — brighter, cleaner
    annotations = [
        (140, "#3fb950", "Context usage"),
        (300, FG, "Session cost"),
        (450, "#fbbf24", "5-hour quota"),
        (620, "#fb923c", "7-day quota"),
        (800, MUTED, "Request timing"),
    ]

    arrow_top = 170
    arrow_bottom = 200
    label_y = 210

    for x, color, text in annotations:
        # Vertical line
        d.line([(x, arrow_top), (x, arrow_bottom)], fill=color, width=2)
        # Small dot at top
        d.ellipse([(x - 3, arrow_top - 3), (x + 3, arrow_top + 3)], fill=color)
        # Label
        d.text((x - 40, label_y), text, font=font(MONO, 13), fill=color)

    # Bottom quote
    d.text((60, H - 70), 'This single line prevents 90% of "why is Claude slow?" moments.',
           font=font(SANS, 16), fill=MUTED)

    save(img, "terminal-statusline.png")


# ─── Image 5: Quote Card (improved — stronger presence) ───────────

def generate_quote():
    """Shareable quote card — bolder, more personality."""
    W, H = 1200, 630
    img, d = new_canvas(W, H)

    # Top and bottom accent bars
    d.rectangle([(0, 0), (W, 6)], fill=ACCENT)
    d.rectangle([(0, H - 6), (W, H)], fill=ACCENT)

    # Large quotation mark — much bolder
    d.text((40, -10), "\u201c", font=font(SANS, 280), fill=ACCENT)

    # Quote text
    lines = [
        "Every hour invested",
        "in the setup saves",
        "ten hours downstream.",
    ]
    y = 170
    for line in lines:
        d.text((80, y), line, font=font(SANS, 58), fill=FG)
        y += 75

    # Sub-line — italic feel via smaller size
    d.text((80, y + 25), "And building the system is more fun", font=font(SANS, 26), fill=MUTED)
    d.text((80, y + 58), "than most of the tasks it automates.", font=font(SANS, 26), fill=MUTED)

    # Author block
    author_y = H - 85
    d.rectangle([(80, author_y), (140, author_y + 3)], fill=ACCENT)
    d.text((80, author_y + 15), "@nikitacometa", font=font(MONO, 18), fill=ACCENT)
    d.text((260, author_y + 15), "·", font=font(MONO, 18), fill=MUTED)
    d.text((285, author_y + 15), "nikitacometa.dev", font=font(MONO, 18), fill=MUTED)

    save(img, "quote-card.png")


# ─── Main ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating blog post images (v2)...")
    generate_stats_hero()
    generate_layers()
    generate_before_after()
    generate_terminal()
    generate_quote()
    print("Done!")
