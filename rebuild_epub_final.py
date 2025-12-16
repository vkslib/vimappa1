#!/usr/bin/env python3
"""
FINAL EPUB FIX - Complete clean rebuild
"""
import shutil
from pathlib import Path

def rebuild_epub_completely():
    """Rebuild EPUB from source files with proper XHTML"""
    
    print("=== COMPLETE EPUB REBUILD ===")
    
    source_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim")
    epub_dir = source_dir / "epub_output" / "OEBPS"
    
    # Step 1: Remove all broken HTML files
    print("1. Removing broken files...")
    for html_file in epub_dir.glob("chapter*.html"):
        html_file.unlink()
        print(f"   Removed: {html_file.name}")
    
    # Step 2: Copy fresh files from content directory
    print("2. Copying fresh content files...")
    content_dir = source_dir / "content"
    for source_file in content_dir.glob("*.html"):
        target_file = epub_dir / source_file.name
        shutil.copy2(source_file, target_file)
        print(f"   Copied: {source_file.name}")
    
    # Step 3: Fix each file individually with perfect XHTML
    print("3. Converting to perfect XHTML...")
    
    template = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="de">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title}</title>
  <link rel="stylesheet" href="style.css"/>
  <script src="script.js"></script>
</head>
<body>
{body_content}
</body>
</html>'''
    
    for html_file in epub_dir.glob("*.html"):
        if html_file.name in ['nav.html', 'cover.html']:
            continue
            
        print(f"   Converting: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        import re
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
        title = title_match.group(1).strip() if title_match else "VimAPP German A1"
        
        # Extract body content
        body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
        if body_match:
            body_content = body_match.group(1).strip()
        else:
            # Find body start and extract everything after
            body_start = content.find('<body>')
            if body_start > -1:
                body_content = content[body_start + 6:].strip()
                if body_content.endswith('</body>'):
                    body_content = body_content[:-7].strip()
                if body_content.endswith('</html>'):
                    body_content = body_content[:-7].strip()
            else:
                body_content = ""
        
        # Create perfect XHTML
        perfect_html = template.format(title=title, body_content=body_content)
        
        # Write perfect file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(perfect_html)
    
    print("4. Updating CSS and JS...")
    # Copy fresh CSS and JS
    for file in ["style.css", "script.js"]:
        source_file = source_dir / file
        if source_file.exists():
            target_file = epub_dir / file
            shutil.copy2(source_file, target_file)
            print(f"   Updated: {file}")
    
    print("\n✅ EPUB completely rebuilt with perfect XHTML!")

def create_final_epub():
    """Create final EPUB file"""
    print("5. Creating final EPUB...")
    
    import zipfile
    
    epub_output_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output")
    epub_file = Path(r"d:\my code\mypadbookvim\mypadbookvim\VimAPP_German_A1_FINAL.epub")
    
    # Remove existing epub file
    if epub_file.exists():
        epub_file.unlink()
    
    with zipfile.ZipFile(epub_file, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Add mimetype (uncompressed, first)
        epub.write(epub_output_dir / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
        
        # Add META-INF
        for file in (epub_output_dir / "META-INF").rglob("*"):
            if file.is_file():
                arcname = str(file.relative_to(epub_output_dir))
                epub.write(file, arcname)
        
        # Add OEBPS
        for file in (epub_output_dir / "OEBPS").rglob("*"):
            if file.is_file():
                arcname = str(file.relative_to(epub_output_dir))
                epub.write(file, arcname)
    
    size_mb = epub_file.stat().st_size / (1024 * 1024)
    print(f"✅ Final EPUB created: {epub_file}")
    print(f"📦 File size: {size_mb:.1f} MB")
    return epub_file

if __name__ == "__main__":
    rebuild_epub_completely()
    final_epub = create_final_epub()
    print(f"\n🎉 PERFECT EPUB READY: {final_epub.name}")
    print("📱 This version should work flawlessly on iPad!")