---
layout: single
title: "About"
permalink: /about/
author_profile: true
classes: wide
---

<!-- Force browser refresh and fix issues -->
<style>
  /* Hide default page title */
  .page__title { display: none !important; }
  .page__meta { display: none !important; }
  
  /* FORCE FIX: Author profile photo overlay issue */
  .sidebar .author__avatar img,
  .author__avatar img {
    transition: none !important;
    opacity: 1 !important;
    filter: none !important;
    transform: none !important;
  }
  
  .sidebar .author__avatar::before,
  .sidebar .author__avatar::after,
  .author__avatar::before,
  .author__avatar::after {
    display: none !important;
    content: none !important;
  }
  
  .sidebar .author__avatar:hover img,
  .author__avatar:hover img {
    opacity: 1 !important;
    filter: none !important;
    transform: none !important;
  }
  
  /* FORCE FIX: Responsive card grid that actually works */
  .about-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)) !important;
    gap: 1.5rem !important;
    margin: 2rem 0 !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  
  .about-card {
    background: white !important;
    padding: 1.5rem !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07) !important;
    border: 1px solid #e9ecef !important;
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
  
  .about-card-icon {
    font-size: 2rem !important;
    margin-bottom: 0.8rem !important;
    display: block !important;
    line-height: 1 !important;
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
  
  /* Force mobile responsiveness */
  @media (max-width: 768px) {
    .about-grid {
      grid-template-columns: 1fr !important;
      gap: 1rem !important;
    }
    
    .about-card {
      padding: 1.2rem !important;
    }
  }
  
  /* Override any conflicting styles */
  .page__content .about-grid {
    display: grid !important;
  }
  
  /* Force container to be properly sized */
  .page__content {
    overflow-x: hidden !important;
  }
</style>

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 5rem 2rem; margin: 0 0 4rem 0; text-align: center; border-radius: 0 0 30px 30px; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
  <h1 style="font-size: 4rem; font-weight: 700; margin-bottom: 1.5rem; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.1); letter-spacing: -0.02em;">Hello, I'm Tao Xu</h1>
  <p style="font-size: 1.5rem; font-weight: 400; opacity: 0.95; max-width: 600px; margin: 0 auto;">Passionate about technology, innovation, and creating meaningful digital experiences</p>
</div>

<div style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
  
<h2 style="font-size: 2.5rem; font-weight: 600; color: #2d3748; margin: 3rem 0 2rem 0; text-align: center;">
  <span style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">What I Do</span>
</h2>

<div class="about-grid">
  
<div class="about-card">
  <span class="about-card-icon">📊</span>
  <h3>Project Management</h3>
  <p>Leading tech and security projects across APAC with PMP certification, delivering measurable impact through agile methodologies.</p>
</div>

<div class="about-card">
  <span class="about-card-icon">🤖</span>
  <h3>AI & Data Science</h3>
  <p>Specialized in Large Language Models, neural networks, and compliance frameworks. Research published in CCLD 2024.</p>
</div>

<div class="about-card">
  <span class="about-card-icon">🔒</span>
  <h3>Security & Compliance</h3>
  <p>Expert in compliance frameworks including GDPR, NIST, AI Act, TC260-003, and WDTA for safe AI deployment.</p>
</div>

<div class="about-card">
  <span class="about-card-icon">💻</span>
  <h3>Technical Expertise</h3>
  <p>Full-stack development with Python, R, JavaScript, TypeScript, and modern frameworks. Data science with PyTorch.</p>
</div>

<div class="about-card">
  <span class="about-card-icon">🌏</span>
  <h3>APAC Leadership</h3>
  <p>Cross-cultural project leadership across Australia, China, and Singapore. Fluent in English and Mandarin.</p>
</div>

<div class="about-card">
  <span class="about-card-icon">🎓</span>
  <h3>Research & Education</h3>
  <p>Master's in Data Science from Australian National University (QS:32), Bachelor's in Management from UCD (QS:118).</p>
</div>

</div>

<h2 style="font-size: 2.5rem; font-weight: 600; color: #2d3748; margin: 4rem 0 2rem 0; text-align: center;">
  <span style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">My Journey</span>
</h2>

<div style="background: white; padding: 2.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07); margin: 2rem 0;">
<p style="font-size: 1.1rem; line-height: 1.7; color: #4a5568; margin: 0;">
Welcome to my personal space on the web. Here, you'll find insights into my professional journey, thoughts on technology, and the projects I'm passionate about. I believe in the power of technology to transform lives and create positive impact.
</p>
</div>

<h2 style="font-size: 2.5rem; font-weight: 600; color: #2d3748; margin: 4rem 0 2rem 0; text-align: center;">
  <span style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Let's Connect</span>
</h2>

<div style="background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%); color: white; padding: 3rem 2rem; border-radius: 20px; text-align: center; margin: 3rem 0;">
  <h3 style="font-size: 1.8rem; font-weight: 600; margin-bottom: 1rem; color: white;">Ready to Collaborate?</h3>
  <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 2rem; max-width: 500px; margin-left: auto; margin-right: auto;">
    I'm always excited to connect with like-minded individuals and explore new opportunities for collaboration and growth.
  </p>
  <a href="/contact/" style="display: inline-block; background: white; color: #0984e3; padding: 1rem 2rem; border-radius: 25px; text-decoration: none; font-weight: 600; transition: all 0.3s ease;">
    Get in Touch
  </a>
</div>

</div>

<!-- Force refresh cache -->
<script>
// Add timestamp to force cache invalidation
document.head.insertAdjacentHTML('beforeend', '<meta name="cache-control" content="no-cache, no-store, must-revalidate">');
</script> 