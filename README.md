# Tao Xu | Personal Portfolio

Personal website at [taoxee.github.io](https://taoxee.github.io) — Jekyll static site with Apple-inspired design, bilingual EN/ZH support, and scroll animations.

## Features

### Design & UX
- Apple-inspired aesthetic: Inter font, `#007AFF` blue, clean white cards
- Collapsible author sidebar with arrow toggle, state persisted in `localStorage`
- Scroll reveal animations site-wide (fade + stagger) via native `IntersectionObserver`
- Lucide-style SVG icons — no emoji, no external icon fonts for custom elements
- Responsive layouts at 1024px and 1280px breakpoints

### Internationalization
- Bilingual EN / ZH toggle with 120+ translation keys
- `data-translate` attributes on all user-facing text
- Google Translate fallback for additional languages
- Language preference persisted in `localStorage`

### Content
- LinkedIn social posts feed (`_data/social_posts.yml`)
- Certificate PDF carousel (Swiper.js)
- CV PDF downloads: English + Chinese
- Posts sandbox page (`/posts-v2/`) with dark tech hero, dot-grid, blinking cursor, animated post counter

### Technical
- Google Analytics GA4 (G-XQZWYLLV49)
- Iconify CDN for brand icons
- WeChat ID clipboard copy with tooltip feedback

## Stack

| Layer | Choice |
|-------|--------|
| Generator | Jekyll 3.10 (github-pages 232) |
| Theme | `mmistakes/minimal-mistakes@4.26.1`, skin: `air` |
| Hosting | GitHub Pages |
| CSS | Custom SCSS (~1700 lines) in `assets/css/main.scss` |
| JS | Vanilla ES5 — translation engine, IntersectionObserver reveal, sidebar toggle |

## Local Development

**Requires Homebrew Ruby 3.3** (system macOS Ruby 2.6 is too old for the gems).

Add to `~/.zshrc` (once):
```bash
export PATH="/opt/homebrew/opt/ruby@3.3/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:$PATH"
```

Then:
```bash
bundle install
bundle exec jekyll serve --port 4000
# Visit http://localhost:4000
```

## Key Files

| File | Purpose |
|------|---------|
| `_config.yml` | Site config, author profile |
| `assets/css/main.scss` | All custom styles (~1700 lines) |
| `_includes/head/custom.html` | Meta tags, sidebar/icon/tooltip CSS |
| `_includes/scripts.html` | EN/ZH translation dict, Google Translate, scroll reveal JS |
| `_includes/sidebar.html` | Collapsible author sidebar |
| `_includes/linkedin-post-card.html` | Social post card component |
| `_data/social_posts.yml` | LinkedIn post content |
| `_data/navigation.yml` | Site nav |
| `_pages/about.md` | About page |
| `_pages/cv.md` | CV with Swiper certificate carousel |
| `_pages/posts.md` | Posts page |
| `_pages/posts-v2.md` | Tech-style posts sandbox |
| `_pages/contact.md` | Contact page with WeChat clipboard copy |

## Site Structure

```
/about/      Personal background, skills grid, CTA
/cv/         Resume download, certificates carousel, skills, education
/posts/      LinkedIn posts feed, category pills
/posts-v2/   Tech-style sandbox: dark hero, dot-grid, animated counter
/contact/    Email, LinkedIn, GitHub, WeChat
```

## Deployment

Pushed to `main` → auto-deployed via GitHub Pages.

**Live**: [https://taoxee.github.io](https://taoxee.github.io)
