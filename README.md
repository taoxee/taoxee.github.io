# Tao Xu | Personal Website

[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-brightgreen)](https://taoxee.github.io/)
[![Jekyll](https://img.shields.io/badge/Built%20with-Jekyll-red)](https://jekyllrb.com/)
[![Minimal Mistakes](https://img.shields.io/badge/Theme-Minimal%20Mistakes-blue)](https://mmistakes.github.io/minimal-mistakes/)

> A modern, Apple-inspired personal website featuring a clean design, professional portfolio, and BBS-style blog.

## 🌟 Features

### 📱 Apple-Inspired Design
- Clean, minimal aesthetic inspired by Apple's design language
- Smooth animations and hover effects
- Responsive design that works on all devices
- Dark mode support following system preferences

### 🏠 Homepage
- Hero section with gradient background
- Interactive feature cards
- Clear call-to-action buttons
- Recent posts preview

### 👤 About & Bio Pages
- Professional introduction and background
- Skills and expertise showcase
- Personal philosophy and interests
- Journey and experience timeline

### 📄 CV/Resume Section
- Professional experience and qualifications
- Downloadable PDF resume
- Skills categorized by technology stack
- Education and certifications
- Achievement highlights

### 📝 BBS-Style Posts
- Modern take on bulletin board system posting
- Categories and tags for organization
- Clean, readable post layouts
- Comment integration ready

### 📞 Contact Page
- Multiple contact methods
- Contact form integration
- Professional social links
- Response time expectations

## 🚀 Technology Stack

- **Framework**: Jekyll 4.x
- **Theme**: Minimal Mistakes (customized)
- **Styling**: SCSS with Apple-inspired custom styles
- **Hosting**: GitHub Pages
- **Forms**: Formspree integration ready
- **Analytics**: Google Analytics integrated

## 🛠️ Setup & Development

### Prerequisites
- Ruby 2.7+ 
- Bundler
- Git

### Local Development
```bash
# Clone the repository
git clone https://github.com/taoxee/taoxee.github.io.git
cd taoxee.github.io

# Install dependencies
bundle install

# Run local development server
bundle exec jekyll serve

# Access the site at http://localhost:4000
```

### Building for Production
```bash
# Build the site
bundle exec jekyll build

# Output will be in _site/ directory
```

## 📁 Project Structure

```
taoxee.github.io/
├── _config.yml          # Jekyll configuration
├── _data/
│   └── navigation.yml   # Site navigation
├── _includes/           # Reusable components
├── _layouts/            # Page layouts
├── _pages/              # Static pages
│   ├── about.md
│   ├── bio.md
│   ├── cv.md
│   ├── posts.md
│   └── contact.md
├── _posts/              # Blog posts
├── _sass/               # SCSS stylesheets
├── assets/
│   ├── css/
│   ├── files/           # CV and documents
│   └── images/          # Images and media
└── index.html           # Homepage
```

## 🎨 Customization

### Colors
The site uses Apple-inspired colors:
- Primary Blue: `#007AFF`
- Dark Text: `#1d1d1f`
- Light Gray: `#666`
- Background: `#fafafa`

### Typography
- Font Family: `-apple-system, BlinkMacSystemFont, 'Segoe UI'...`
- Optimized for readability across all devices
- Proper font weights (300, 500, 600, 700)

### Components
- Gradient hero sections
- Card-based layouts
- Smooth hover animations
- Apple-style buttons and forms

## 📋 Content Management

### Adding New Posts
1. Create a new file in `_posts/` with format: `YYYY-MM-DD-title.md`
2. Include front matter with title, date, categories, and tags
3. Write content in Markdown
4. Commit and push to publish

### Updating CV
1. Replace the PDF file in `assets/files/`
2. Update the CV page content in `_pages/cv.md`
3. Update the "last updated" date

### Personalizing Content
1. Update `_config.yml` with your information
2. Replace placeholder content in pages
3. Add your profile photo to `assets/images/`
4. Update social links and contact information

## 🚀 Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch.

### Manual Deployment
```bash
# Commit changes
git add .
git commit -m "Update content"
git push origin main

# GitHub Pages will automatically build and deploy
```

## 📞 Contact & Support

- **Email**: your.email@example.com
- **GitHub**: [@taoxee](https://github.com/taoxee)
- **LinkedIn**: [Your Profile](https://linkedin.com/in/yourprofile)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Minimal Mistakes Theme](https://mmistakes.github.io/minimal-mistakes/) by Michael Rose
- [Jekyll](https://jekyllrb.com/) static site generator
- [GitHub Pages](https://pages.github.com/) for hosting
- Apple's design principles for inspiration

---

*Built with ❤️ and powered by Jekyll & GitHub Pages*
