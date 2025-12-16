#!/usr/bin/env python3
"""
Create EPUB3 from HTML textbook
"""
import os
import shutil
import zipfile
from pathlib import Path
import re

def copy_files():
    """Copy all necessary files to EPUB structure (skip if already exists)"""
    source_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim")
    epub_dir = source_dir / "epub_output" / "OEBPS"
    
    # Copy content files only if they don't exist (to preserve XHTML fixes)
    content_dir = source_dir / "content"
    if content_dir.exists():
        for file in content_dir.glob("*.html"):
            target_file = epub_dir / file.name
            if not target_file.exists():
                print(f"  Copying new file: {file.name}")
                shutil.copy2(file, target_file)
            else:
                print(f"  Keeping existing: {file.name}")
    
    # Copy CSS and JS (always update these)
    for file in ["style.css", "script.js"]:
        if (source_dir / file).exists():
            shutil.copy2(source_dir / file, epub_dir / file)
    
    # Copy audio directory (always update)
    audio_source = source_dir / "audio"
    audio_dest = epub_dir / "audio"
    if audio_source.exists():
        if audio_dest.exists():
            shutil.rmtree(audio_dest)
        shutil.copytree(audio_source, audio_dest)
    
    return epub_dir

def fix_html_for_epub(epub_dir):
    """Fix HTML files for EPUB3 compatibility"""
    for html_file in epub_dir.glob("*.html"):
        if html_file.name in ["nav.html", "cover.html"]:
            continue
            
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add EPUB3 namespace
        content = content.replace(
            '<html lang="de">',
            '<html xmlns="http://www.w3.org/1999/xhtml" lang="de">'
        )
        
        # Fix relative paths for EPUB structure
        content = content.replace('href="../style.css"', 'href="style.css"')
        content = content.replace('src="../script.js"', 'src="script.js"')
        
        # Ensure proper DOCTYPE
        if not content.startswith('<!DOCTYPE html>'):
            content = '<!DOCTYPE html>\n' + content
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

def generate_audio_manifest(epub_dir):
    """Generate audio file entries for content.opf"""
    audio_dir = epub_dir / "audio"
    audio_items = []
    
    if audio_dir.exists():
        for subdir in ["vocab", "sentences", "dialogues"]:
            subdir_path = audio_dir / subdir
            if subdir_path.exists():
                for audio_file in subdir_path.glob("*.mp3"):
                    relative_path = f"audio/{subdir}/{audio_file.name}"
                    file_id = f"audio_{subdir}_{audio_file.stem}"
                    audio_items.append(
                        f'        <item id="{file_id}" href="{relative_path}" media-type="audio/mpeg"/>'
                    )
    
    return '\n'.join(audio_items)

def update_content_opf(epub_dir):
    """Update content.opf with audio files"""
    opf_file = epub_dir / "content.opf"
    
    with open(opf_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate audio manifest
    audio_manifest = generate_audio_manifest(epub_dir)
    
    # Insert audio items before closing manifest tag
    content = content.replace(
        '        <!-- Audio Files (will be added by script) -->',
        audio_manifest
    )
    
    with open(opf_file, 'w', encoding='utf-8') as f:
        f.write(content)

def create_epub():
    """Create the final EPUB file"""
    epub_output_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output")
    epub_file = Path(r"d:\my code\mypadbookvim\mypadbookvim\VimAPP_German_A1.epub")
    
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
    
    return epub_file

def main():
    print("Creating EPUB3 for VimAPP German A1...")
    
    # Step 1: Copy files
    print("1. Copying files...")
    epub_dir = copy_files()
    
    # Step 2: Fix HTML for EPUB3
    print("2. Converting HTML for EPUB3...")
    fix_html_for_epub(epub_dir)
    
    # Step 3: Update content.opf with audio files
    print("3. Updating manifest with audio files...")
    update_content_opf(epub_dir)
    
    # Step 4: Create EPUB file
    print("4. Creating EPUB file...")
    epub_file = create_epub()
    
    print(f"✅ EPUB3 created: {epub_file}")
    print(f"📱 Ready for iPad!")
    
    # Show file size
    size_mb = epub_file.stat().st_size / (1024 * 1024)
    print(f"📦 File size: {size_mb:.1f} MB")

if __name__ == "__main__":
    main()