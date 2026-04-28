# The AI Blueprint - Jekyll SEO-Optimized Site

A high-authority AI resource platform built with Jekyll for programmatic SEO (pSEO). Fully bilingual (English/Spanish) with schema markup, optimized structure, and thousands of potential pages.

## 🚀 Features

- **Programmatic SEO**: Generate 1000+ pages from structured data
- **Bilingual Support**: English (en) and Spanish (es) with automatic redirects
- **Schema Markup**: JSON-LD structured data for rich snippets
- **Responsive Design**: Mobile-first, Tailwind-inspired CSS
- **Jekyll-Ready**: Uses Jekyll collections and data files for automation
- **SEO Optimized**: Meta tags, canonical URLs, sitemaps, and more

## 📁 Project Structure

```
├── _config.yml                # Jekyll configuration with SEO settings
├── _data/
│   ├── tools.yml             # AI tools data (GPT, Claude, Gemini, Llama)
│   └── industries.yml        # Target industries for spoke articles
├── _includes/
│   ├── header.html          # Navigation and language toggle
│   ├── footer.html          # Footer with links
│   └── schema.html          # Schema markup templates
├── _layouts/
│   ├── default.html         # Main layout with SEO
│   ├── page.html            # Page template
│   └── post.html            # Blog post template
├── _sass/
│   └── main.scss            # Global styles (Tailwind-inspired)
├── assets/
│   ├── css/
│   │   └── main.scss        # CSS entry point
│   ├── js/
│   │   └── main.js          # JavaScript utilities
│   └── images/              # Logos, icons, OG images
├── en/
│   ├── index.md             # English homepage
│   └── pillars/
│       └── gpt.md           # ChatGPT pillar page
├── es/
│   ├── index.md             # Spanish homepage
│   └── pilares/
│       └── gpt.md           # Spanish ChatGPT pillar page
└── index.html               # Root redirect based on language preference
```

## 🛠️ Setup Instructions

### Prerequisites
- Ruby 2.7+
- Jekyll 4.0+
- Bundler

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LD1878/testingdeepseekforpro.git
   cd testingdeepseekforpro
   ```

2. **Install dependencies**
   ```bash
   bundle install
   ```

3. **Update `_config.yml`**
   - Change `url` to your domain
   - Add Google Analytics ID if desired
   - Update author and contact info

4. **Build and serve locally**
   ```bash
   bundle exec jekyll serve
   ```

   Visit `http://localhost:4000` to preview your site.

## 📝 Creating Content

### Adding a New Pillar Page (Tool)

Create a file at `en/pillars/[tool-name].md`:

```markdown
---
layout: page
lang: en
title: "Tool Name: Comprehensive Guide"
description: "SEO description here"
schema_type: "HowTo"
permalink: /en/pillars/tool-name.html
---

# Tool Name Content

Your content here...
```

Then add the same for Spanish at `es/pilares/[tool-name].md`

### Adding a Spoke Article (Tool + Industry)

Create a file at `en/guides/[tool]-[industry].md`:

```markdown
---
layout: page
lang: en
title: "[Tool] for [Industry]"
description: "How to use [Tool] in [Industry]"
schema_type: "HowTo"
permalink: /en/guides/[tool]-[industry].html
---

Content connecting tool to specific industry use cases...
```

### Adding News/Blog Posts

Create a file at `_posts/YYYY-MM-DD-title.md`:

```markdown
---
layout: post
lang: en
title: "Post Title"
date: 2026-04-28
tags: ["ai", "news"]
---

Post content here...
```

## 🔍 SEO Best Practices

### On-Page SEO
- ✅ Unique meta descriptions (< 160 chars)
- ✅ H1 tag (only one per page)
- ✅ Internal linking (spoke to pillar pages)
- ✅ Schema markup for rich snippets
- ✅ Mobile-responsive design
- ✅ Fast page load time

### Technical SEO
- ✅ Sitemap auto-generated (`sitemap.xml`)
- ✅ RSS feed (`feed.xml`)
- ✅ Canonical URLs to prevent duplicates
- ✅ Language hreflang tags (en/es)
- ✅ robots.txt included
- ✅ Structured data (JSON-LD)

### Content Strategy
- **Pillar Pages**: Comprehensive guides for each AI tool (4 tools)
- **Spoke Articles**: Specific guides for Tool + Industry combinations (4 × 7 = 28 articles)
- **Topic Clusters**: Internal linking creates topical authority
- **Long-tail Keywords**: Automatically optimized through combinations

## 🌍 Bilingual Setup

The site automatically handles language routing:

1. **Root redirects** based on browser language preference (stored in localStorage)
2. **Language toggle** in header for manual switching
3. **Separate content** for `/en/` and `/es/` paths
4. **hreflang tags** inform search engines about language versions

To add new content:
1. Create English version at `/en/path/to/page.md`
2. Create Spanish version at `/es/path/to/page.md`
3. Ensure `lang:` is set correctly in front matter

## 📊 Google Analytics & Tracking

To enable analytics:

1. Add your Google Analytics ID to `_config.yml`
2. Update the `_includes/analytics.html` file with your tracking code
3. Include the analytics snippet in your layout

## 🚀 Deploying to GitHub Pages

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to repo Settings → Pages
   - Set source to `main` branch
   - Your site will be live at `https://yourusername.github.io/testingdeepseekforpro`

3. **Update `_config.yml`**
   ```yaml
   url: "https://yourusername.github.io"
   baseurl: "/testingdeepseekforpro"  # if it's a project repo
   ```

## 🔧 Customization

### Colors
Edit `_sass/main.scss` variables:
```scss
$primary: #10a37f;
$secondary: #3b82f6;
$accent: #f59e0b;
```

### Fonts
Update font families in `_sass/main.scss`:
```scss
$font-family-sans: "Your Font Here", sans-serif;
```

### Layout
Modify `_layouts/default.html` to customize header/footer appearance.

## 📈 Programmatic Content Generation

The site is designed to auto-generate combinations:

**Example**: 4 AI Tools × 7 Industries = **28 potential spoke articles**

To enable this, create a generator script in `scripts/generate-pages.py`:

```python
import yaml

# Load data
with open('_data/tools.yml') as f:
    tools = yaml.safe_load(f)

with open('_data/industries.yml') as f:
    industries = yaml.safe_load(f)

# Generate combinations
for tool in tools:
    for industry in industries:
        filename = f"en/guides/{tool['slug']['en']}-{industry['slug']['en']}.md"
        # Write markdown file...
```

## 📚 Resources

- [Jekyll Documentation](https://jekyllrb.com/)
- [SEO Best Practices](https://developers.google.com/search)
- [Schema.org Markup](https://schema.org/)
- [GitHub Pages Docs](https://pages.github.com/)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## 📧 Support

For questions or issues, contact [hello@theaiblueprint.com](mailto:hello@theaiblueprint.com)

---

**Built with ❤️ for AI Professionals**
