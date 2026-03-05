import type { APIRoute } from "astro";

export const GET: APIRoute = async () => {
  const markdownContent = `# Nikita Gorokhov (@nikitacometa)

Developer, meditator, standup comic. Building with AI from Koh Phangan.

## Navigation

- [About](/about.md)
- [Recent Posts](/posts.md)
- [Archives](/archives.md)
- [RSS Feed](/rss.xml)

## Links

- Twitter: [@NikitaCometa](https://twitter.com/NikitaCometa)
- GitHub: [@nikitacometa](https://github.com/nikitacometa)
- Telegram: [@cometablog](https://t.me/cometablog)
- Instagram: [@nikita.cometa](https://instagram.com/nikita.cometa)

---

*This is the markdown-only version of nikitacometa.dev. Visit [nikitacometa.dev](https://nikitacometa.dev) for the full experience.*`;

  return new Response(markdownContent, {
    status: 200,
    headers: {
      "Content-Type": "text/markdown; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
};
