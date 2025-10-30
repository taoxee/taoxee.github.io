---
layout: single # changes page layout
title: "About" # changes page title
permalink: /about/ # changes page URL
author_profile: true # shows/hides author profile
classes: wide # changes page width/layout
---

<!-- 
OLD DUPLICATED CSS - MOVED TO assets/css/main.scss
TODO: Remove this commented block after confirming new CSS classes work

<style>
  .page__title { display: none !important; }
  .page__meta { display: none !important; }
  
  /* Author profile photo overlay fix */
  .sidebar .author__avatar img,
  .author__avatar img {
    transition: none !important; /* image transition */
    opacity: 1 !important;       /* image opacity */
    filter: none !important;     /* image filter */
    transform: none !important;  /* image transform */
  }
  
  .sidebar .author__avatar::before,
  .sidebar .author__avatar::after,
  .author__avatar::before,
  .author__avatar::after {
    display: none !important;    /* pseudo-element display */
    content: none !important;    /* pseudo-element content */
  }
  
  .sidebar .author__avatar:hover img,
  .author__avatar:hover img {
    opacity: 1 !important;       /* hover opacity */
    filter: none !important;     /* hover filter */
    transform: none !important;  /* hover transform */
  }
  
  /* Card grid */
  .about-grid {
    display: grid !important; /* grid/flex layout */
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)) !important; /* card min width/columns */
    gap: 1.5rem !important; /* space between cards */
    margin: 2rem 0 !important; /* grid margin */
    width: 100% !important; /* grid width */
    max-width: 100% !important; /* max grid width */
  }
  
  .about-card {
    background: white !important; /* card background */
    padding: 1.2rem 1.2rem; /* card padding */
    border-radius: 12px !important; /* card border radius */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07) !important; /* card shadow */
    border: 4px solid #e9ecef !important; /* card border */
    transition: transform 0.3s ease, box-shadow 0.3s ease !important; /* card transition */
    min-height: 180px !important; /* min card height */
    max-height: none !important; /* max card height */
    display: flex !important; /* card layout */
    flex-direction: column !important; /* card flex direction */
    overflow: hidden !important; /* card overflow */
    word-wrap: break-word !important; /* word wrap */
    box-sizing: border-box !important; /* box sizing */
  }
  
  .about-card:hover {
    transform: translateY(-2px) !important; /* hover move */
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15) !important; /* hover shadow */
  }
  
  .about-card-icon {
    font-size: 2rem !important; /* icon size */
    margin-bottom: 0.8rem !important; /* icon margin */
    display: block !important; /* icon display */
    line-height: 1 !important; /* icon line height */
  }
  
  .about-card h3 {
    color: #007AFF !important; /* heading color */
    margin: 0 0 0.8rem 0 !important; /* heading margin */
    font-size: 1.2rem !important; /* heading size */
    font-weight: 600 !important; /* heading weight */
    line-height: 1.3 !important; /* heading line height */
    word-wrap: break-word !important; /* heading wrap */
  }
  
  .about-card p {
    color: #666 !important; /* text color */
    line-height: 1.5 !important; /* text line height */
    font-size: 0.95rem !important; /* text size */
    flex-grow: 1 !important; /* text flex grow */
    margin: 0 !important; /* text margin */
    overflow: hidden !important; /* text overflow */
    word-wrap: break-word !important; /* text wrap */
    hyphens: auto !important; /* text hyphenation */
  }
  
  /* Mobile responsiveness */
  @media (max-width: 768px) { /* mobile breakpoint */
    .about-grid {
      grid-template-columns: 1fr !important; /* single column */
      gap: 1rem !important; /* mobile gap */
    }
    .about-card {
      padding: 1.2rem !important; /* mobile card padding */
    }
  }
  
  /* Force grid in content */
  .page__content .about-grid {
    display: grid !important; /* force grid */
  }
  
  .page__content {
    overflow-x: hidden !important;
  }
</style>
-->

<div class="hero-section hero-section--about">
  <h1 class="hero__title">Hello, I'm Tao Xu</h1>
  <p class="hero__subtitle">Passionate about technology, innovation, and creating meaningful digital experiences</p>
  <div class="hero-buttons">
    <a href="/contact/" class="hero-btn">
      <span data-translate="Contact Me">Contact Me</span>
    </a>
    <a href="/cv/" class="hero-btn">
      <span data-translate="View My CV">View My CV</span>
    </a>
  </div>
</div>

<div style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
  
<h2 style="font-size: 2.5rem; font-weight: 600; color: #2d3748; margin: 3rem 0 2rem 0; text-align: center;">
  <span style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">What I Do</span>
</h2>

  
<div class="about-grid">
  <!-- CHANGED: Icons moved inside h3 tags -->
  <div class="about-card">
    <h3><span class="icon">📊</span> <span data-translate="Project Management">Project Management</span></h3>
    <p>Leading tech and security projects across APAC with PMP certification, delivering measurable impact through agile methodologies.</p>
  </div>
  <div class="about-card">
    <h3><span class="icon">🤖</span> <span data-translate="AI & Data Science">AI & Data Science</span></h3>
    <p>Specialized in Large Language Models, neural networks, and compliance frameworks. Research published in CCLD 2024.</p>
  </div>
  <div class="about-card">
    <h3><span class="icon">🔒</span> <span data-translate="Security & Compliance">Security & Compliance</span></h3>
    <p>Expert in compliance frameworks including GDPR, NIST, AI Act, TC260-003, and WDTA for safe AI deployment.</p>
  </div>
  <div class="about-card">
    <h3><span class="icon">💻</span> <span data-translate="Technical Expertise">Technical Expertise</span></h3>
    <p>Full-stack development with Python, R, JavaScript, TypeScript, and modern frameworks. Data science with PyTorch.</p>
  </div>
  <div class="about-card">
    <h3><span class="icon">🌏</span> <span data-translate="APAC Leadership">APAC Leadership</span></h3>
    <p>Cross-cultural project leadership across Australia, China, and Singapore. Fluent in English and Mandarin.</p>
  </div>
  <div class="about-card">
    <h3><span class="icon">🎓</span> <span data-translate="Research & Education">Research & Education</span></h3>
    <p>Master's in Data Science from Australian National University (QS:32), Bachelor's in Management from UCD (QS:118).</p>
  </div>
</div>

</div>

<h2 style="font-size: 2.5rem; font-weight: 600; color: #2d3748; margin: 4rem 0 2rem 0; text-align: center;">
  <span style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">My Journey</span>
</h2>

<div class="about-card">
  <h3 style="display: flex; align-items: center; justify-content: center;">
    <span class="icon" style="margin-right: 0.5em;">❤️</span>
    <span data-translate="Hi There!">Hi There!</span>
  </h3>
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

<!-- Force refresh cache -->
<script>
// Add timestamp to force cache invalidation
document.head.insertAdjacentHTML('beforeend', '<meta name="cache-control" content="no-cache, no-store, must-revalidate">');
</script> 