---
layout: single
title: "Contact"
permalink: /contact/
author_profile: true
classes: wide
---

<!-- 
OLD DUPLICATED CSS - MOVED TO assets/css/main.scss
TODO: Remove this commented block after confirming new CSS classes work

<style>
  .page__title { display: none !important; }
  .page__meta { display: none !important; }
  
  .about-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)) !important;
    gap: 1.5rem !important;
    margin: 3rem 0 !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  
  .about-card {
    background: white !important;
    padding: 1.2rem 1.2rem !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07) !important;
    border: 4px solid #e9ecef !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    min-height: 180px !important;
    max-height: none !important;
    display: flex !important;
    flex-direction: column !important;
    overflow: hidden !important;
    word-wrap: break-word !important;
    box-sizing: border-box !important;
  }
  
  .about-card:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15) !important;
  }
  
  .about-card h3 {
    color: #007AFF !important;
    margin: 0 0 0.8rem 0 !important;
    font-size: 1.2rem !important;
    font-weight: 600 !important;
    line-height: 1.3 !important;
    word-wrap: break-word !important;
  }
  
  .about-card p {
    color: #666 !important;
    line-height: 1.5 !important;
    font-size: 0.95rem !important;
    flex-grow: 1 !important;
    margin: 0 !important;
    overflow: hidden !important;
    word-wrap: break-word !important;
    hyphens: auto !important;
  }
  
  @media (max-width: 768px) {
    .about-grid {
      grid-template-columns: 1fr !important;
      gap: 1rem !important;
    }
    .about-card {
      padding: 1.2rem !important;
    }
  }
</style>
-->

<div class="hero-section hero-section--contact">
  <h1 class="hero__title">Let's Connect</h1>
  <p class="hero__subtitle">I'd love to hear from you</p>
</div>

<!-- OLD INLINE STYLES - REPLACED WITH CSS CLASSES
TODO: Remove after confirming new classes work

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 5rem 2rem; margin: 0 0 4rem 0; text-align: center; border-radius: 0 0 30px 30px; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
  <h1 style="font-size: 4rem; font-weight: 700; margin-bottom: 1.5rem; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.1); letter-spacing: -0.02em;">Let's Connect</h1>
  <p style="font-size: 1.5rem; font-weight: 400; opacity: 0.95; max-width: 600px; margin: 0 auto;">I'd love to hear from you</p>
</div>
-->

<div class="content-container">

<h2 class="section-title section-title--contact">
  <span class="gradient-text">Get in Touch</span>
</h2>

<!-- OLD INLINE STYLES - REPLACED WITH CSS CLASSES
TODO: Remove after confirming new classes work

<div style="max-width: 800px; margin: 0 auto; padding: 0 2rem;">
<h2 style="font-size: 2.5rem; font-weight: 600; color: #2d3748; margin: 3rem 0 2rem 0; text-align: center;">
  <span style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Get in Touch</span>
</h2>
-->

<div class="about-grid">

<div class="about-card contact-card">
  <div class="contact-card__icon">📧</div>
  <h3 class="contact-card__title">Email</h3>
  <p class="contact-card__description">For professional inquiries and collaborations</p>
  <a href="mailto:xutao1486@gmail.com" class="contact-card__link">
    xutao1486@gmail.com
  </a>
</div>

<!-- <div class="about-card contact-card">
  <div class="contact-card__icon">🌍</div>
  <h3 class="contact-card__title">Work Authorization</h3>
  <p class="contact-card__description">Legally authorized to work in</p>
  <div class="work-auth">
    <div>🇨🇳 China</div>
    <div>🇸🇬 Singapore</div>
    <div>🇦🇺 Australia</div>
    <div>💻 Remote</div>
  </div>
</div> -->

<div class="about-card contact-card">
  <div class="contact-card__icon">
    <img src="/assets/images/linkedin-logo.svg" alt="LinkedIn" width="40" height="40">
  </div>
  <h3 class="contact-card__title">LinkedIn</h3>
  <p class="contact-card__description">Connect with me professionally</p>
  <a href="https://www.linkedin.com/in/tao-xee" target="_blank" class="contact-card__link">
    <span class="iconify" data-icon="tabler:brand-linkedin"></span> Tao Xu
  </a>
</div>

<div class="about-card contact-card">
  <div class="contact-card__icon">
    <img src="/assets/images/github-logo.svg" alt="GitHub" width="40" height="40">
  </div>
  <h3 class="contact-card__title">GitHub</h3>
  <p class="contact-card__description">Check out my code and projects</p>
  <a href="https://github.com/taoxee" target="_blank" class="contact-card__link">
    <img src="/assets/images/github-logo.svg" alt="GitHub" width="16" height="16" style="vertical-align: middle; margin-right: 0.5rem;"> taoxee
  </a>
</div>

<div class="about-card contact-card">
  <div class="contact-card__icon">
    <img src="/assets/images/wechat-logo.svg" alt="WeChat" width="48" height="48">
  </div>
  <h3 class="contact-card__title">WeChat</h3>
  <p class="contact-card__description">Connect via WeChat</p>
  <div class="contact-card__link">
    <span class="iconify" data-icon="mingcute:wechat-line"></span> TaoXee
  </div>
</div>

</div>

<h2 class="section-title section-title--contact">
  <span class="gradient-text">Send a Message</span>
</h2>

<div class="about-card">
  
<form action="https://formspree.io/f/xutao1486@gmail.com" method="POST" class="contact-form">
  
  <div class="form-row">
    <div>
      <label for="name" class="form-label">Name</label>
      <input type="text" id="name" name="name" required class="form-input">
    </div>
    <div>
      <label for="email" class="form-label">Email</label>
      <input type="email" id="email" name="email" required class="form-input">
    </div>
  </div>
  
  <div>
    <label for="subject" class="form-label">Subject</label>
    <input type="text" id="subject" name="subject" required class="form-input">
  </div>
  
  <div>
    <label for="message" class="form-label">Message</label>
    <textarea id="message" name="message" rows="6" required class="form-textarea"></textarea>
  </div>
  
  <button type="submit" class="btn btn--submit">
    Send Message
  </button>
  
</form>

<!-- OLD FORM STYLES - REPLACED WITH CSS CLASSES
TODO: Remove after confirming new classes work

<form action="https://formspree.io/f/xutao1486@gmail.com" method="POST" style="display: grid; gap: 1.5rem;">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
    <div>
      <label for="name" style="display: block; margin-bottom: 0.5rem; color: #2d3748; font-weight: 600;">Name</label>
      <input type="text" id="name" name="name" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1rem; transition: border-color 0.2s;">
    </div>
    <div>
      <label for="email" style="display: block; margin-bottom: 0.5rem; color: #2d3748; font-weight: 600;">Email</label>
      <input type="email" id="email" name="email" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1rem; transition: border-color 0.2s;">
    </div>
  </div>
  <div>
    <label for="subject" style="display: block; margin-bottom: 0.5rem; color: #2d3748; font-weight: 600;">Subject</label>
    <input type="text" id="subject" name="subject" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1rem; transition: border-color 0.2s;">
  </div>
  <div>
    <label for="message" style="display: block; margin-bottom: 0.5rem; color: #2d3748; font-weight: 600;">Message</label>
    <textarea id="message" name="message" rows="6" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1rem; resize: vertical; transition: border-color 0.2s;"></textarea>
  </div>
  <button type="submit" style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 1rem 2rem; border: none; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: transform 0.2s; box-shadow: 0 4px 6px rgba(102, 126, 234, 0.3);">
    Send Message
  </button>
</form>
-->

</div>

<div class="about-card quick-response">
  <h3 style="color: #2d3748; margin-bottom: 1rem;">Quick Response</h3>
  <p style="color: #666; margin-bottom: 1.5rem;">I typically respond to messages within 24 hours. For urgent matters, please reach out via email or LinkedIn.</p>
  
  <div class="quick-response__actions">
    <a href="mailto:xutao1486@gmail.com" class="btn btn--blue">
      Quick Email
    </a>
    <a href="https://www.linkedin.com/in/tao-xee" target="_blank" class="btn btn--linkedin">
      LinkedIn Message
    </a>
  </div>
</div>

<!-- OLD QUICK RESPONSE STYLES - REPLACED WITH CSS CLASSES
TODO: Remove after confirming new classes work

<div class="about-card" style="text-align: center; background: #f8f9fa;">
  <h3 style="color: #2d3748; margin-bottom: 1rem;">Quick Response</h3>
  <p style="color: #666; margin-bottom: 1.5rem;">I typically respond to messages within 24 hours. For urgent matters, please reach out via email or LinkedIn.</p>
  <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
    <a href="mailto:xutao1486@gmail.com" style="background: #007AFF; color: white; padding: 0.75rem 1.5rem; border-radius: 25px; text-decoration: none; font-weight: 600; transition: background 0.2s;">Quick Email</a>
    <a href="https://www.linkedin.com/in/tao-xee" target="_blank" style="background: #0077B5; color: white; padding: 0.75rem 1.5rem; border-radius: 25px; text-decoration: none; font-weight: 600; transition: background 0.2s;">LinkedIn Message</a>
  </div>
</div>
-->

</div>

<!-- <style>
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
</style>  -->