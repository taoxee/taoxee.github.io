---
layout: posts
title: "Posts"
permalink: /posts/
author_profile: true
entries_layout: list
classes: wide
---

<!-- Hide default page title -->
<style>
  .page__title { display: none !important; }
  .page__meta { display: none !important; }
  .archive__title { display: none !important; }
  .archive__subtitle { display: none !important; }
</style>

<div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); color: white; padding: 5rem 2rem; margin: 0 0 4rem 0; text-align: center; border-radius: 0 0 30px 30px; box-shadow: 0 10px 30px rgba(250, 112, 154, 0.3);">
  <h1 style="font-size: 4rem; font-weight: 700; margin-bottom: 1.5rem; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.1); letter-spacing: -0.02em;">Posts & Thoughts</h1>
  <p style="font-size: 1.5rem; font-weight: 400; opacity: 0.95; max-width: 600px; margin: 0 auto;">Sharing insights, experiences, and discoveries</p>
</div>

<div style="max-width: 900px; margin: 0 auto; padding: 0 2rem;">

<div style="background: #f8f9fa; padding: 2rem; border-radius: 16px; margin-bottom: 3rem; text-align: center; border: 1px solid #e9ecef;">
  <h2 style="color: #007AFF; margin-bottom: 1rem; font-size: 1.5rem;">Welcome to My Digital Journal</h2>
  <p style="color: #666; margin-bottom: 2rem; line-height: 1.6;">Here you'll find my thoughts on technology, career insights, project updates, and personal reflections. Think of it as a modern bulletin board where I share what's on my mind.</p>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 2rem;">
    <div style="background: white; padding: 1rem; border-radius: 8px;">
      <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">💭</div>
      <h4 style="color: #007AFF; font-size: 0.9rem;">Tech Insights</h4>
    </div>
    <div style="background: white; padding: 1rem; border-radius: 8px;">
      <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🚀</div>
      <h4 style="color: #007AFF; font-size: 0.9rem;">Project Updates</h4>
    </div>
    <div style="background: white; padding: 1rem; border-radius: 8px;">
      <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📚</div>
      <h4 style="color: #007AFF; font-size: 0.9rem;">Learning Notes</h4>
    </div>
    <div style="background: white; padding: 1rem; border-radius: 8px;">
      <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🌟</div>
      <h4 style="color: #007AFF; font-size: 0.9rem;">Life & Career</h4>
    </div>
  </div>
</div>

<h2 style="font-size: 2.5rem; font-weight: 600; color: #2d3748; margin: 3rem 0 2rem 0; text-align: center; position: relative;">
  <span style="background: linear-gradient(135deg, #fa709a, #fee140); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Recent Posts</span>
</h2>

<div id="posts-container">
  <!-- Posts will be automatically populated here by Jekyll -->
</div>

<div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07); margin: 3rem 0; text-align: center;">
  <h3 style="color: #007AFF; margin-bottom: 1rem;">No Posts Yet?</h3>
  <p style="color: #666; margin-bottom: 2rem;">I'm just getting started! Check back soon for fresh content, or feel free to reach out with topics you'd like me to explore.</p>
  <a href="/contact/" style="display: inline-block; background: #e8f5e8; color: #2e7d32; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.3s ease; cursor: pointer; border: 1px solid #c8e6c9;" onmouseover="this.style.backgroundColor='#c8e6c9'; this.style.transform='translateY(-2px)'" onmouseout="this.style.backgroundColor='#e8f5e8'; this.style.transform='translateY(0)'">
      Suggest a Topic
  </a>
</div>

## Categories

<div style="display: flex; flex-wrap: wrap; gap: 1rem; margin: 2rem 0; justify-content: center;">
  <span style="background: #e3f2fd; color: #1976d2; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 500;">Technology</span>
  <span style="background: #e8f5e8; color: #2e7d32; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 500;">Career</span>
  <span style="background: #fff3e0; color: #f57c00; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 500;">Projects</span>
  <span style="background: #fce4ec; color: #c2185b; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 500;">Learning</span>
  <span style="background: #f3e5f5; color: #7b1fa2; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 500;">Life</span>
</div>

</div>

<style>
  .page__content h2 {
    color: #1d1d1f;
    font-weight: 600;
    font-size: 2rem;
    margin-top: 3rem;
    margin-bottom: 1.5rem;
    border-bottom: 2px solid #007AFF;
    padding-bottom: 0.5rem;
  }
  
  .page__content h3 {
    color: #333;
    font-weight: 600;
    font-size: 1.5rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
  }
  
  .page__content h4 {
    font-weight: 600;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
  }
  
  .page__content p {
    font-size: 1.1rem;
    line-height: 1.7;
    color: #515151;
  }
  
  .page__content {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  }
  
  .entries-list .list__item {
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    margin-bottom: 2rem;
    padding: 2rem;
    transition: transform 0.3s ease;
  }
  
  .entries-list .list__item:hover {
    transform: translateY(-4px);
  }
  
  .entries-list .list__item .archive__item-title {
    color: #007AFF;
    font-weight: 600;
  }
</style> 