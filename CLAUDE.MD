# nikitacometa.dev

Personal dev blog for Nikita Gorokhov (@nikitacometa / @NikitaCometa).
Astro 5 + Tailwind 4 + MDX + Pagefind search. Forked from steipete/steipete.me.

## Commands

```bash
npm run build        # production build → dist/ (use this to verify changes)
npm run preview      # preview production build
npm run lint         # biome lint
npm run format       # biome format
npm run deploy       # build + rsync to Hostinger VPS
```

IMPORTANT: Do NOT run `npm run dev` in agent mode — creates an endless loop.

## Content

Posts live in `src/content/blog/YYYY/slug.md` (or `.mdx` for interactive content).

### Post frontmatter

```yaml
---
author: Nikita Gorokhov
pubDatetime: 2026-03-06T10:00:00Z
title: "Post Title"
featured: false
draft: true
tags: [claude-code, ai]
description: "SEO description, 150-160 chars ideal"
heroImage: "/images/hero.jpg"
---
```

### Writing style

- English for all blog posts (EN audience: Twitter, dev community)
- Technical but accessible — non-developers should understand the value
- Builder perspective: show process and results, not hype
- Specific numbers, dates, examples — never vague
- Self-deprecating humor welcome, guru tone forbidden

## Deployment

Static site hosted on Hostinger VPS (nginx). Build → rsync.

## Domain

- **nikitacometa.dev** — Namecheap, DNS → Hostinger VPS
- SSL: Let's Encrypt via Certbot

## Cross-Platform Content Flow

Blog is the EN hub:
- Blog post → Twitter thread (@NikitaCometa)
- Blog post → adapted TG post (RU, @cometablog)
- Blog post → IG carousel if visual (RU, @nikita.cometa)

## Tech Stack

- Astro 5 + MDX
- Tailwind CSS 4
- React 19 (interactive components)
- Pagefind (client-side search)
- Satori (dynamic OG images)
- Biome (lint + format)
