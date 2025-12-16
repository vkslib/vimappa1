#!/usr/bin/env python3
"""
Create Single HTML File - All-in-one German A1 Textbook
"""
import os
import base64
from pathlib import Path
import mimetypes

def create_single_html():
    """Create single HTML file with embedded CSS, JS, and audio"""
    
    print("🔥 Creating Single HTML File 🔥")
    
    # Paths
    base_dir = Path(".")
    content_dir = base_dir / "content"
    audio_dir = base_dir / "audio"
    
    # Read CSS
    print("📄 Reading CSS...")
    css_content = ""
    css_file = base_dir / "style.css"
    if css_file.exists():
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
    
    # Read JS
    print("📄 Reading JavaScript...")
    js_content = ""
    js_file = base_dir / "script.js"
    if js_file.exists():
        with open(js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()
    
    # Read all chapter contents
    print("📚 Reading chapters...")
    chapters = {}
    for i in range(15):  # chapters 0-14
        chapter_file = content_dir / f"chapter{i:02d}.html"
        if chapter_file.exists():
            with open(chapter_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract body content
            import re
            body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
            if body_match:
                body_content = body_match.group(1).strip()
                chapters[f"chapter{i:02d}"] = {
                    'title': f'Unit {i}: ' + get_chapter_title(content),
                    'content': body_content
                }
    
    # Convert audio files to base64
    print("🎵 Converting audio files...")
    audio_data = {}
    total_audio_size = 0
    
    if audio_dir.exists():
        for category in ['vocab', 'sentences', 'dialogues']:
            cat_dir = audio_dir / category
            if cat_dir.exists():
                for mp3_file in cat_dir.glob("*.mp3"):
                    with open(mp3_file, 'rb') as f:
                        audio_bytes = f.read()
                        audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')
                        audio_key = f"{category}/{mp3_file.name}"
                        audio_data[audio_key] = f"data:audio/mp3;base64,{audio_b64}"
                        total_audio_size += len(audio_bytes)
    
    print(f"🎵 Converted {len(audio_data)} audio files ({total_audio_size / 1024 / 1024:.1f} MB)")
    
    # Create single HTML
    print("🔨 Building single HTML file...")
    
    html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VimAPP German A1 - Complete Interactive Textbook</title>
    <style>
        /* Embedded CSS */
        {css_content}
        
        /* Single file specific styles */
        .chapter {{
            display: none;
            padding: 20px;
        }}
        
        .chapter.active {{
            display: block;
        }}
        
        .chapter-nav {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: var(--primary);
            color: white;
            padding: 10px;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .chapter-nav select {{
            padding: 8px 12px;
            border: none;
            border-radius: 5px;
            background: white;
            margin-right: 10px;
        }}
        
        .chapter-nav .nav-buttons {{
            float: right;
        }}
        
        .nav-btn {{
            background: rgba(255,255,255,0.2);
            color: white;
            border: 1px solid rgba(255,255,255,0.3);
            padding: 5px 15px;
            margin: 0 2px;
            border-radius: 3px;
            cursor: pointer;
        }}
        
        .nav-btn:hover {{
            background: rgba(255,255,255,0.3);
        }}
        
        .nav-btn:disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}
        
        .content-wrapper {{
            margin-top: 60px;
            padding: 20px;
        }}
        
        /* iPad specific */
        @media screen and (max-width: 1024px) {{
            .content-wrapper {{
                margin-top: 80px;
                padding: 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="chapter-nav">
        <select id="chapterSelect" onchange="switchChapter(this.value)">
            {generate_chapter_options(chapters)}
        </select>
        
        <div class="nav-buttons">
            <button class="nav-btn" onclick="previousChapter()" id="prevBtn">← ก่อนหน้า</button>
            <button class="nav-btn" onclick="nextChapter()" id="nextBtn">ถัดไป →</button>
        </div>
        
        <div style="clear: both;"></div>
    </div>
    
    <div class="content-wrapper">
        {generate_chapters_html(chapters)}
    </div>

    <script>
        // Audio data embedded
        const audioData = {audio_data_js(audio_data)};
        
        // Navigation
        let currentChapter = 0;
        const totalChapters = {len(chapters)};
        
        function switchChapter(chapterKey) {{
            // Hide all chapters
            document.querySelectorAll('.chapter').forEach(ch => ch.classList.remove('active'));
            
            // Show selected chapter
            const targetChapter = document.getElementById(chapterKey);
            if (targetChapter) {{
                targetChapter.classList.add('active');
                currentChapter = parseInt(chapterKey.replace('chapter', ''));
                updateNavButtons();
            }}
        }}
        
        function previousChapter() {{
            if (currentChapter > 0) {{
                const prevKey = 'chapter' + String(currentChapter - 1).padStart(2, '0');
                document.getElementById('chapterSelect').value = prevKey;
                switchChapter(prevKey);
            }}
        }}
        
        function nextChapter() {{
            if (currentChapter < totalChapters - 1) {{
                const nextKey = 'chapter' + String(currentChapter + 1).padStart(2, '0');
                document.getElementById('chapterSelect').value = nextKey;
                switchChapter(nextKey);
            }}
        }}
        
        function updateNavButtons() {{
            document.getElementById('prevBtn').disabled = (currentChapter === 0);
            document.getElementById('nextBtn').disabled = (currentChapter === totalChapters - 1);
        }}
        
        // Audio playback function
        function play(audioPath) {{
            const cleanPath = audioPath.replace('../audio/', '');
            if (audioData[cleanPath]) {{
                const audio = new Audio(audioData[cleanPath]);
                audio.play().catch(e => {{
                    console.log('Audio play failed:', e);
                    alert('เสียงไม่สามารถเล่นได้ อาจเป็นเพราะบราวเซอร์ป้องกัน autoplay');
                }});
            }} else {{
                console.log('Audio not found:', cleanPath);
            }}
        }}
        
        // Initialize
        document.addEventListener('DOMContentLoaded', function() {{
            switchChapter('chapter00');
            updateNavButtons();
        }});
        
        // Embedded JavaScript
        {js_content}
    </script>
</body>
</html>"""
    
    # Write to file
    output_file = base_dir / "VimAPP_German_A1_Complete.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    file_size = output_file.stat().st_size / 1024 / 1024
    print(f"✅ Single HTML file created!")
    print(f"📁 File: {output_file.name}")
    print(f"📊 Size: {file_size:.1f} MB")
    print(f"🎵 Audio files: {len(audio_data)}")
    print(f"📚 Chapters: {len(chapters)}")
    
    return output_file

def get_chapter_title(content):
    """Extract chapter title from HTML"""
    import re
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    if title_match:
        return title_match.group(1).strip()
    return "German Lesson"

def generate_chapter_options(chapters):
    """Generate select options for chapters"""
    options = ""
    for key, chapter in chapters.items():
        options += f'<option value="{key}">{chapter["title"]}</option>\\n'
    return options

def generate_chapters_html(chapters):
    """Generate HTML for all chapters"""
    html = ""
    for key, chapter in chapters.items():
        active_class = "active" if key == "chapter00" else ""
        html += f'''
        <div id="{key}" class="chapter {active_class}">
            <h1>{chapter["title"]}</h1>
            {chapter["content"]}
        </div>
        '''
    return html

def audio_data_js(audio_data):
    """Convert audio data to JavaScript object"""
    import json
    return json.dumps(audio_data, indent=2)

if __name__ == "__main__":
    create_single_html()
    print("\\n🎉 Ready to use on iPad!")
    print("📱 Copy the HTML file to iPad Files app and open with Safari")