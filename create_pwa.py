#!/usr/bin/env python3
"""
Create PWA Structure - Progressive Web App for German A1
"""
import shutil
from pathlib import Path

def create_pwa_structure():
    """Create complete PWA file structure"""
    
    print("🚀 Creating PWA Structure 🚀")
    
    base_dir = Path(".")
    pwa_dir = base_dir / "pwa"
    
    # Create directories
    directories = [
        "chapters",
        "icons", 
        "screenshots",
        "audio/vocab",
        "audio/sentences", 
        "audio/dialogues"
    ]
    
    for dir_name in directories:
        (pwa_dir / dir_name).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created: {dir_name}")
    
    # Copy CSS and JS
    print("📄 Copying assets...")
    
    # Copy main files
    files_to_copy = [
        ("style.css", "style.css"),
        ("script.js", "script.js")
    ]
    
    for src, dst in files_to_copy:
        src_file = base_dir / src
        if src_file.exists():
            shutil.copy2(src_file, pwa_dir / dst)
            print(f"  ✅ {src} → {dst}")
    
    # Copy chapter files
    print("📚 Copying chapters...")
    content_dir = base_dir / "content"
    
    for i in range(15):  # chapters 0-14
        chapter_file = content_dir / f"chapter{i:02d}.html"
        if chapter_file.exists():
            # Read and modify chapter content for PWA
            with open(chapter_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add PWA-specific modifications
            pwa_content = modify_chapter_for_pwa(content, i)
            
            # Write to PWA chapters directory
            pwa_chapter_file = pwa_dir / "chapters" / f"chapter{i:02d}.html"
            with open(pwa_chapter_file, 'w', encoding='utf-8') as f:
                f.write(pwa_content)
            
            print(f"  ✅ Chapter {i:02d}")
    
    # Copy audio files
    print("🎵 Copying audio files...")
    audio_src_dir = base_dir / "audio"
    audio_dst_dir = pwa_dir / "audio"
    
    if audio_src_dir.exists():
        total_files = 0
        for category in ['vocab', 'sentences', 'dialogues']:
            src_cat_dir = audio_src_dir / category
            dst_cat_dir = audio_dst_dir / category
            
            if src_cat_dir.exists():
                for mp3_file in src_cat_dir.glob("*.mp3"):
                    shutil.copy2(mp3_file, dst_cat_dir / mp3_file.name)
                    total_files += 1
        
        print(f"  🎵 Copied {total_files} audio files")
    
    # Generate basic icons (placeholder)
    print("🎨 Creating placeholder icons...")
    create_placeholder_icons(pwa_dir / "icons")
    
    print(f"\n✅ PWA Structure Created!")
    print(f"📁 Location: {pwa_dir}")
    print(f"📱 Ready for deployment!")
    
    return pwa_dir

def modify_chapter_for_pwa(content, chapter_num):
    """Modify chapter HTML for PWA compatibility"""
    
    # Add PWA-specific header
    pwa_header = f'''<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#2563eb">
    <title>Unit {chapter_num} - VimAPP German A1</title>
    <link rel="stylesheet" href="../style.css">
    <style>
        /* PWA Chapter Styles */
        .chapter-nav {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: var(--primary);
            color: white;
            padding: 10px 20px;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .nav-home {{
            color: white;
            text-decoration: none;
            font-weight: bold;
        }}
        
        .nav-controls {{
            display: flex;
            gap: 10px;
        }}
        
        .nav-btn {{
            background: rgba(255,255,255,0.2);
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 3px;
            cursor: pointer;
            text-decoration: none;
            font-size: 14px;
        }}
        
        .nav-btn:hover {{
            background: rgba(255,255,255,0.3);
        }}
        
        .content-wrapper {{
            margin-top: 60px;
            padding: 20px;
        }}
        
        /* Notes feature */
        .notes-panel {{
            position: fixed;
            right: -300px;
            top: 60px;
            bottom: 0;
            width: 300px;
            background: white;
            box-shadow: -2px 0 10px rgba(0,0,0,0.1);
            transition: right 0.3s ease;
            z-index: 999;
            padding: 20px;
            overflow-y: auto;
        }}
        
        .notes-panel.open {{
            right: 0;
        }}
        
        .notes-toggle {{
            position: fixed;
            right: 20px;
            bottom: 20px;
            background: var(--primary);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1001;
        }}
        
        @media (max-width: 768px) {{
            .notes-panel {{
                width: 100%;
                right: -100%;
            }}
            
            .content-wrapper {{
                padding: 10px;
            }}
        }}
    </style>
</head>
<body>
    <nav class="chapter-nav">
        <a href="../index.html" class="nav-home">🏠 VimAPP German A1</a>
        <div class="nav-controls">
            <a href="chapter{max(0, chapter_num-1):02d}.html" class="nav-btn">← ก่อนหน้า</a>
            <a href="chapter{min(14, chapter_num+1):02d}.html" class="nav-btn">ถัดไป →</a>
        </div>
    </nav>
    
    <div class="content-wrapper">'''
    
    # Extract body content
    import re
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
    if body_match:
        body_content = body_match.group(1).strip()
    else:
        body_content = content
    
    # Add notes panel
    notes_panel = '''
    </div>
    
    <!-- Notes Panel -->
    <div class="notes-panel" id="notes-panel">
        <h3>📝 บันทึกของฉัน</h3>
        <textarea id="notes-content" placeholder="เขียนบันทึกที่นี่..." 
                  style="width: 100%; height: 200px; border: 1px solid #ddd; border-radius: 5px; padding: 10px;">
        </textarea>
        <button onclick="saveNotes()" style="margin-top: 10px; padding: 8px 16px; background: var(--primary); color: white; border: none; border-radius: 4px;">💾 บันทึก</button>
        <button onclick="clearNotes()" style="margin-top: 10px; margin-left: 10px; padding: 8px 16px; background: var(--warning); color: white; border: none; border-radius: 4px;">🗑️ ลบ</button>
    </div>
    
    <button class="notes-toggle" onclick="toggleNotes()" title="เปิด/ปิดบันทึก">
        📝
    </button>
    
    <script src="../script.js"></script>
    <script>
        // Notes functionality
        function toggleNotes() {
            const panel = document.getElementById('notes-panel');
            panel.classList.toggle('open');
            loadNotes();
        }
        
        function saveNotes() {
            const content = document.getElementById('notes-content').value;
            localStorage.setItem('notes_chapter''' + str(chapter_num).zfill(2) + '''', content);
            alert('✅ บันทึกแล้ว!');
        }
        
        function loadNotes() {
            const saved = localStorage.getItem('notes_chapter''' + str(chapter_num).zfill(2) + '''');
            if (saved) {
                document.getElementById('notes-content').value = saved;
            }
        }
        
        function clearNotes() {
            if (confirm('คุณต้องการลบบันทึกใช่หรือไม่?')) {
                document.getElementById('notes-content').value = '';
                localStorage.removeItem('notes_chapter''' + str(chapter_num).zfill(2) + '''');
                alert('🗑️ ลบแล้ว!');
            }
        }
        
        // Update progress
        function updateProgress() {
            localStorage.setItem('progress_chapter''' + str(chapter_num).zfill(2) + '''', '100');
        }
        
        // Auto-load notes on page load
        document.addEventListener('DOMContentLoaded', loadNotes);
        
        // Mark as visited
        setTimeout(updateProgress, 5000);
    </script>
</body>
</html>'''
    
    return pwa_header + body_content + notes_panel

def create_placeholder_icons(icons_dir):
    """Create placeholder icon files (you'd normally use real icons)"""
    
    sizes = [16, 32, 72, 96, 128, 144, 152, 192, 384, 512]
    
    # Create simple placeholder text files (in real scenario, use proper PNG icons)
    for size in sizes:
        icon_file = icons_dir / f"icon-{size}x{size}.png"
        
        # Create a simple placeholder file
        with open(icon_file, 'w') as f:
            f.write(f"# Placeholder icon {size}x{size}\n# Replace with actual PNG file")
        
        print(f"  📦 icon-{size}x{size}.png")

if __name__ == "__main__":
    pwa_dir = create_pwa_structure()
    
    print(f"\n🎯 Next Steps:")
    print(f"1. Replace placeholder icons in {pwa_dir}/icons/")
    print(f"2. Test PWA: Open {pwa_dir}/index.html in browser")
    print(f"3. Deploy to GitHub Pages or web server")
    print(f"4. Add to Home Screen on mobile device")
    print(f"\n🚀 PWA Ready!")