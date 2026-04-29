---
layout: posts
title: "Posts"
permalink: /posts/
author_profile: true
entries_layout: list
classes: wide
---

<div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); color: white; padding: 4rem 2rem 3rem; margin: 0 0 3rem 0; text-align: center; border-radius: 0 0 30px 30px; box-shadow: 0 10px 30px rgba(255, 154, 158, 0.3);">
  <h1 style="font-size: 3.5rem; font-weight: 700; margin-bottom: 1rem; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.1); letter-spacing: -0.02em;" data-translate="Posts & Thoughts">Posts & Thoughts</h1>
  <p style="font-size: 1.5rem; font-weight: 400; opacity: 0.95; max-width: 600px; margin: 0 auto 2rem;" data-translate="posts_hero_subtitle">Sharing insights, experiences, and discoveries</p>
  <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; opacity: 0.95;">

    <span style="display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.95rem; font-weight: 500;">
      <!-- chat bubble / tech -->
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      Tech
    </span>

    <span style="display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.95rem; font-weight: 500;">
      <!-- rocket / projects -->
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>
      Projects
    </span>

    <span style="display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.95rem; font-weight: 500;">
      <!-- book / learning -->
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
      Learning
    </span>

    <span style="display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.95rem; font-weight: 500;">
      <!-- star / career -->
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      Career
    </span>

  </div>
</div>

<div style="max-width: 900px; margin: 0 auto; padding: 0 2rem;">

{% assign social_posts = site.data.social_posts | default: empty_array %}
{% assign has_social = false %}
{% if social_posts and social_posts.size > 0 %}
  {% assign has_social = true %}
{% endif %}
{% assign has_jekyll = false %}
{% if site.posts and site.posts.size > 0 %}
  {% assign has_jekyll = true %}
{% endif %}

<div id="posts-container" style="margin: 2rem 0;">
  {% if has_social %}
    {% assign sorted_posts = social_posts | sort: "date" | reverse %}
    {% for li_post in sorted_posts %}
      {% include linkedin-post-card.html post=li_post %}
    {% endfor %}
  {% endif %}
</div>

{% unless has_social or has_jekyll %}
<div class="about-card" style="text-align: center; margin: 3rem 0;">
  <p style="margin-bottom: 0.75rem; color: #9aa0a6;"><svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg></p>
  <h3 style="color: #2d3748;" data-translate="No Posts Yet?">Nothing here yet</h3>
  <p style="color: #666; margin-bottom: 2rem;" data-translate="posts_no_posts_desc">Check back soon — or suggest a topic you'd like me to write about.</p>
  <a href="/contact/" style="display: inline-block; background: linear-gradient(135deg, #ff9a9e, #fecfef) !important; color: white !important; padding: 0.75rem 1.5rem; border-radius: 20px; text-decoration: none; font-weight: 600; font-size: 1rem; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(255,154,158,0.3);" onmouseover="this.style.opacity='0.9'; this.style.transform='translateY(-2px)'" onmouseout="this.style.opacity='1'; this.style.transform='translateY(0)'" data-translate="Suggest a Topic">
    Suggest a Topic
  </a>
</div>
{% endunless %}

<script src="/assets/js/linkedin-posts.js"></script>

<h2 style="font-size: 1.75rem; font-weight: 600; color: #2d3748; margin: 4rem 0 1.5rem 0; text-align: center;">
  <span style="background: linear-gradient(135deg, #ff9a9e, #fecfef); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;" data-translate="Categories">Browse by Topic</span>
</h2>

<div style="display: flex; flex-wrap: wrap; gap: 0.75rem; justify-content: center; margin-bottom: 4rem;">
  <span style="background: #e3f2fd; color: #1976d2; padding: 0.6rem 1.25rem; border-radius: 25px; font-weight: 600; font-size: 0.95rem; cursor: pointer; border: 2px solid #bbdefb; transition: all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(25,118,210,0.2)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-0.1em;margin-right:0.3em;"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>Technology</span>
  <span style="background: #e8f5e8; color: #2e7d32; padding: 0.6rem 1.25rem; border-radius: 25px; font-weight: 600; font-size: 0.95rem; cursor: pointer; border: 2px solid #c8e6c9; transition: all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(46,125,50,0.2)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-0.1em;margin-right:0.3em;"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>Career</span>
  <span style="background: #fff3e0; color: #f57c00; padding: 0.6rem 1.25rem; border-radius: 25px; font-weight: 600; font-size: 0.95rem; cursor: pointer; border: 2px solid #ffcc80; transition: all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(245,124,0,0.2)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-0.1em;margin-right:0.3em;"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>Projects</span>
  <span style="background: #fce4ec; color: #c2185b; padding: 0.6rem 1.25rem; border-radius: 25px; font-weight: 600; font-size: 0.95rem; cursor: pointer; border: 2px solid #f8bbd9; transition: all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(194,24,91,0.2)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-0.1em;margin-right:0.3em;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>Learning</span>
  <span style="background: #f3e5f5; color: #7b1fa2; padding: 0.6rem 1.25rem; border-radius: 25px; font-weight: 600; font-size: 0.95rem; cursor: pointer; border: 2px solid #ce93d8; transition: all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(123,31,162,0.2)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-0.1em;margin-right:0.3em;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>Life</span>
</div>

</div>
