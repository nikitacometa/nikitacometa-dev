import { SITE } from "./consts";

export const SOCIALS = [
  {
    name: "Github",
    href: "https://github.com/nikitacometa",
    linkTitle: ` ${SITE.title} on Github`,
    icon: "github",
    active: true,
  },
  {
    name: "X",
    href: "https://x.com/NikitaCometa",
    linkTitle: `${SITE.title} on X`,
    icon: "twitter",
    active: true,
  },
  {
    name: "Instagram",
    href: "https://instagram.com/nikita.cometa",
    linkTitle: `${SITE.title} on Instagram`,
    icon: "instagram",
    active: true,
  },
  {
    name: "Telegram",
    href: "https://t.me/cometablog",
    linkTitle: `${SITE.title} on Telegram`,
    icon: "telegram",
    active: true,
  },
  {
    name: "Mail",
    href: "mailto:nikita@nikitacometa.dev",
    linkTitle: `Send an email to ${SITE.title}`,
    icon: "mail",
    active: true,
  },
] as const;

export const SHARE_LINKS = [
  {
    name: "X",
    href: "https://x.com/intent/post?url=",
    linkTitle: `Share this post on X`,
    icon: "twitter",
  },
  {
    name: "Telegram",
    href: "https://t.me/share/url?url=",
    linkTitle: `Share this post via Telegram`,
    icon: "telegram",
  },
  {
    name: "LinkedIn",
    href: "https://www.linkedin.com/sharing/share-offsite/?url=",
    linkTitle: `Share this post on LinkedIn`,
    icon: "linkedin",
  },
  {
    name: "WhatsApp",
    href: "https://wa.me/?text=",
    linkTitle: `Share this post via WhatsApp`,
    icon: "whatsapp",
  },
  {
    name: "Facebook",
    href: "https://www.facebook.com/sharer.php?u=",
    linkTitle: `Share this post on Facebook`,
    icon: "facebook",
  },
  {
    name: "Mail",
    href: "mailto:?subject=See%20this%20post&body=",
    linkTitle: `Share this post via email`,
    icon: "mail",
  },
] as const;
