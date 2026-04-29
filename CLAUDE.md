# CLAUDE.md — taoxee.github.io

## Project Overview
Personal portfolio site for Tao Xu at https://taoxee.github.io/

**Stack:** Jekyll static site, `remote_theme: mmistakes/minimal-mistakes@4.26.1`, skin: `air`, GitHub Pages deployment.

**Pages:** About (`/about/`), CV (`/cv/`), Posts (`/posts/`), Contact (`/contact/`). Navigation in `_data/navigation.yml`.

**Key custom features:**
- Bilingual EN/ZH translation: `data-translate` attributes + JS dictionary in `_includes/scripts.html`. Google Translate fallback. Language persisted in `localStorage`.
- LinkedIn social posts: data in `_data/social_posts.yml`, rendered via `_includes/linkedin-post-card.html`.
- Certificate PDF carousel on CV page via Swiper.js (CDN).
- CV PDF downloads: English (`/assets/files/PM-TAO-Intl-Apr-15.pdf`), Chinese (`/assets/files/PM-TAO-中文-Dec-12.pdf`).
- Google Analytics: G-XQZWYLLV49 in `_includes/head/custom.html`.
- Iconify for icons (CDN). Apple-inspired styling: Inter font, #007AFF blue.
- Collapsible author sidebar with arrow toggle, localStorage persistence, layout reflow at 1024px and 1280px breakpoints.

**Author config:** `_config.yml` under `author:`.

---

## Working Rules

### Never auto-commit
Only commit when the user explicitly asks. Do not stage or commit after making code changes.

### No co-author in commits
Never add `Co-Authored-By:` trailers to commit messages.

### Work as a UX professional
Before any UI/layout/CSS change, audit all affected modules, breakpoints, and sibling elements for side effects:
1. Identify every layout/page type that renders the affected component (single, archive, posts, wide, etc.)
2. Check each breakpoint where layout rules change (`$large`: 1024px, `$x-large`: 1280px)
3. Verify sibling/parent element behavior at all states
4. Consider: layout reflow, z-index stacking, mobile breakpoints, theme class overrides, animation conflicts

**Why this matters:** The sidebar collapse feature required explicit reflow fixes for both `article.page` and `div.archive` — a silent side effect that wasn't obvious from the initial request.

---

## Key File Map
| File | Purpose |
|------|---------|
| `assets/css/main.scss` | All custom SCSS (~1700 lines) |
| `_includes/head/custom.html` | Custom CSS, meta tags, Google Analytics, sidebar/icon styles |
| `_includes/scripts.html` | EN/ZH translation JS dictionary + Google Translate integration |
| `_includes/sidebar.html` | Collapsible author sidebar with toggle button + JS |
| `_includes/linkedin-post-card.html` | Social post card component |
| `_data/social_posts.yml` | LinkedIn post content |
| `_data/navigation.yml` | Site nav links |
| `_pages/about.md` | About page |
| `_pages/cv.md` | CV page with Swiper carousel |
| `_pages/posts.md` | Posts/archive page |
| `_pages/contact.md` | Contact page with WeChat clipboard copy |
