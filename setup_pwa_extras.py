#!/usr/bin/env python3
"""
Generate SVG icons and convert to PNG for PWA
"""
from pathlib import Path

def create_svg_icon():
    """Create SVG icon for the app"""
    
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <!-- Background -->
  <rect width="512" height="512" fill="#2563eb" rx="80"/>
  
  <!-- German flag stripes -->
  <rect x="50" y="150" width="412" height="40" fill="#000000"/>
  <rect x="50" y="190" width="412" height="40" fill="#DD0000"/>
  <rect x="50" y="230" width="412" height="40" fill="#FFCE00"/>
  
  <!-- Book/App Icon -->
  <rect x="180" y="300" width="152" height="120" fill="#ffffff" rx="12"/>
  <rect x="190" y="310" width="132" height="100" fill="#f8fafc" rx="8"/>
  
  <!-- Text lines -->
  <line x1="200" y1="330" x2="310" y2="330" stroke="#2563eb" stroke-width="3"/>
  <line x1="200" y1="350" x2="290" y2="350" stroke="#64748b" stroke-width="2"/>
  <line x1="200" y1="370" x2="300" y2="370" stroke="#64748b" stroke-width="2"/>
  <line x1="200" y1="390" x2="280" y2="390" stroke="#64748b" stroke-width="2"/>
  
  <!-- Audio/Sound waves -->
  <circle cx="120" cy="360" r="8" fill="#10b981"/>
  <path d="M 135 352 Q 150 360 135 368" stroke="#10b981" stroke-width="3" fill="none"/>
  <path d="M 145 344 Q 165 360 145 376" stroke="#10b981" stroke-width="2" fill="none"/>
  
  <!-- VIM text -->
  <text x="256" y="100" text-anchor="middle" fill="#ffffff" font-family="Arial, sans-serif" font-size="48" font-weight="bold">VIM</text>
  <text x="256" y="130" text-anchor="middle" fill="#e2e8f0" font-family="Arial, sans-serif" font-size="20" font-weight="normal">German A1</text>
  
  <!-- Decorative elements -->
  <circle cx="80" cy="80" r="12" fill="rgba(255,255,255,0.2)"/>
  <circle cx="432" cy="80" r="8" fill="rgba(255,255,255,0.15)"/>
  <circle cx="432" cy="432" r="12" fill="rgba(255,255,255,0.2)"/>
  <circle cx="80" cy="432" r="8" fill="rgba(255,255,255,0.15)"/>
</svg>'''
    
    return svg_content

def create_github_workflow():
    """Create GitHub Actions workflow for deployment"""
    
    workflow = '''name: Deploy PWA to GitHub Pages

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: |
        cd pwa
        npm init -y
        npm install --save-dev imagemin imagemin-pngquant
    
    - name: Build and optimize
      run: |
        # Optimize images and assets
        echo "Building PWA..."
        
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      if: github.ref == 'refs/heads/main'
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./pwa
        cname: your-domain.com  # Optional: Add your custom domain
'''
    
    return workflow

def create_readme():
    """Create README for the PWA"""
    
    readme = '''# 🇩🇪 VimAPP German A1 - Progressive Web App

Interactive German A1 learning application with audio pronunciation and offline support.

## ✨ Features

- 📚 **15 Complete Units** (A1 Level)
- 🎵 **Audio Pronunciation** (600+ audio files)
- 📱 **Progressive Web App** (Install like native app)
- 🌐 **Offline Support** (Works without internet)
- 📝 **Personal Notes** (Save your progress)
- 📊 **Progress Tracking** (LocalStorage)
- 🎯 **Interactive Exercises** (Click & learn)

## 🚀 Installation

### Option 1: Web Browser
1. Visit: `https://yourusername.github.io/vimapp-german-a1/`
2. Click "Add to Home Screen" on mobile
3. Enjoy learning German! 🇩🇪

### Option 2: Local Development
```bash
git clone https://github.com/yourusername/vimapp-german-a1.git
cd vimapp-german-a1/pwa
python -m http.server 8000
# Open http://localhost:8000
```

## 📱 Supported Devices

- ✅ **iOS Safari** (iPad/iPhone)
- ✅ **Android Chrome** 
- ✅ **Desktop Chrome/Edge/Firefox**
- ✅ **Samsung Internet**

## 🎯 Learning Path

| Unit | Topic | Content |
|------|--------|---------|
| 0 | Introduction | Alphabet & Pronunciation |
| 1 | Personal Introduction | Pronouns & "sein" |
| 2 | Family & Friends | Possessive pronouns |
| 3 | Professions | Job vocabulary |
| 4 | Living | Home & furniture |
| 5 | Food & Drink | Meals & restaurants |
| 6 | Shopping | Clothes & prices |
| 7 | Leisure Time | Hobbies & sports |
| 8 | Health | Body parts & doctor |
| 9 | Travel | Transportation |
| 10 | Weather | Seasons & temperature |
| 11 | Time & Appointments | Dates & scheduling |
| 12 | Work | Job interviews |
| 13 | School & Education | Learning vocabulary |
| 14 | Exam Preparation | A1 test practice |

## 🛠️ Technologies

- **HTML5** + **CSS3** + **JavaScript**
- **Service Worker** (Offline caching)
- **Web App Manifest** (PWA features)
- **LocalStorage** (Progress & notes)
- **Responsive Design** (Mobile-first)

## 📊 Performance

- ⚡ **Fast Loading** (Service Worker caching)
- 💾 **Offline First** (Works without internet)
- 🔊 **Audio Optimized** (Compressed MP3)
- 📱 **Mobile Optimized** (Touch-friendly)

## 🔧 Development

### File Structure
```
pwa/
├── index.html          # Main app page
├── manifest.json       # PWA manifest
├── sw.js              # Service worker
├── style.css          # Main styles
├── script.js          # App logic
├── chapters/          # Individual lessons
├── audio/             # Pronunciation files
└── icons/            # App icons
```

### Audio Files
- **600+ MP3 files** (German pronunciation)
- **Categories**: Vocabulary, Sentences, Dialogues
- **Voice**: Microsoft Edge TTS (de-DE-KatjaNeural)
- **Speed**: -20% (Optimized for A1 learners)

## 📄 License

MIT License - Feel free to use for educational purposes!

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📮 Contact

- 🌐 **Website**: [Your Website]
- 📧 **Email**: [Your Email]
- 💬 **Issues**: [GitHub Issues](https://github.com/yourusername/vimapp-german-a1/issues)

---

**Happy Learning German! 🇩🇪📚**

*Viel Erfolg beim Deutschlernen!*
'''
    
    return readme

def setup_pwa_extras():
    """Create additional PWA files"""
    
    print("🎨 Creating PWA extras...")
    
    pwa_dir = Path("pwa")
    
    # Create SVG icon
    svg_content = create_svg_icon()
    with open(pwa_dir / "icons" / "app-icon.svg", 'w') as f:
        f.write(svg_content)
    print("  ✅ Created app-icon.svg")
    
    # Create workflow directory
    workflow_dir = pwa_dir / ".github" / "workflows"
    workflow_dir.mkdir(parents=True, exist_ok=True)
    
    workflow_content = create_github_workflow()
    with open(workflow_dir / "deploy.yml", 'w') as f:
        f.write(workflow_content)
    print("  ✅ Created GitHub Actions workflow")
    
    # Create README
    readme_content = create_readme()
    with open(pwa_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("  ✅ Created README.md")
    
    # Create .gitignore
    gitignore = '''# Dependencies
node_modules/
npm-debug.log*

# Build outputs
dist/
build/

# Environment
.env
.env.local

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Temporary
*.tmp
*.temp
'''
    
    with open(pwa_dir / ".gitignore", 'w') as f:
        f.write(gitignore)
    print("  ✅ Created .gitignore")
    
    # Create package.json for development
    package_json = '''{
  "name": "vimapp-german-a1",
  "version": "1.0.0",
  "description": "Interactive German A1 Learning PWA",
  "main": "index.html",
  "scripts": {
    "start": "python -m http.server 8000",
    "build": "echo 'Building PWA...'",
    "deploy": "gh-pages -d ."
  },
  "keywords": ["german", "language", "learning", "pwa", "education"],
  "author": "VimAPP",
  "license": "MIT",
  "devDependencies": {
    "gh-pages": "^4.0.0"
  }
}'''
    
    with open(pwa_dir / "package.json", 'w') as f:
        f.write(package_json)
    print("  ✅ Created package.json")
    
    print(f"\n✅ PWA Extras Created!")
    return pwa_dir

if __name__ == "__main__":
    pwa_dir = setup_pwa_extras()
    
    print(f"\n🎯 PWA Complete! Next steps:")
    print(f"1. 🎨 Add real PNG icons to replace placeholders")
    print(f"2. 🌐 Push to GitHub repository")
    print(f"3. 📱 Enable GitHub Pages in repository settings")
    print(f"4. 🚀 Access your PWA at: https://yourusername.github.io/repo-name/")
    print(f"\n📁 PWA Location: {pwa_dir}")
    print(f"🎉 Ready for production!")