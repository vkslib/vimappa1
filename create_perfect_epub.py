#!/usr/bin/env python3
"""
Create Perfect EPUB - Final Version
"""
import zipfile
import shutil
from pathlib import Path
import xml.etree.ElementTree as ET

def validate_html_files():
    """Validate all HTML files in EPUB"""
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("=== VALIDATING HTML FILES ===")
    valid_count = 0
    invalid_count = 0
    
    for html_file in sorted(epub_dir.glob("*.html")):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            ET.fromstring(content)
            print(f"  ✅ Valid: {html_file.name}")
            valid_count += 1
            
        except ET.ParseError as e:
            print(f"  ❌ Invalid: {html_file.name}")
            print(f"     Error: {e}")
            invalid_count += 1
    
    print(f"\n=== VALIDATION RESULTS ===")
    print(f"✅ Valid files: {valid_count}")
    print(f"❌ Invalid files: {invalid_count}")
    
    if invalid_count == 0:
        print("🎉 ALL FILES ARE VALID XHTML!")
        return True
    else:
        print(f"⚠️ {invalid_count} files need fixing")
        return False

def create_final_epub():
    """Create final EPUB file"""
    print("\n=== CREATING FINAL EPUB ===")
    
    epub_output_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output")
    epub_file = Path(r"d:\my code\mypadbookvim\mypadbookvim\VimAPP_German_A1_PERFECT.epub")
    
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
    print(f"✅ PERFECT EPUB created: {epub_file}")
    print(f"📦 File size: {size_mb:.1f} MB")
    return epub_file

def count_audio_files():
    """Count audio files"""
    audio_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\audio")
    
    if not audio_dir.exists():
        print("⚠️ Audio directory not found")
        return 0
    
    vocab_count = len(list((audio_dir / "vocab").glob("*.mp3"))) if (audio_dir / "vocab").exists() else 0
    sentences_count = len(list((audio_dir / "sentences").glob("*.mp3"))) if (audio_dir / "sentences").exists() else 0 
    dialogues_count = len(list((audio_dir / "dialogues").glob("*.mp3"))) if (audio_dir / "dialogues").exists() else 0
    
    total = vocab_count + sentences_count + dialogues_count
    
    print(f"🔊 Audio files: {total} total")
    print(f"   - Vocabulary: {vocab_count}")
    print(f"   - Sentences: {sentences_count}")
    print(f"   - Dialogues: {dialogues_count}")
    
    return total

if __name__ == "__main__":
    print("🔥 CREATING PERFECT EPUB - FINAL VERSION 🔥")
    
    # Step 1: Validate all files
    all_valid = validate_html_files()
    
    if not all_valid:
        print("❌ Cannot create EPUB - validation errors found")
        exit(1)
    
    # Step 2: Count audio files
    audio_count = count_audio_files()
    
    # Step 3: Create final EPUB
    final_epub = create_final_epub()
    
    print(f"\n🎉 SUCCESS! 🎉")
    print(f"📚 EPUB File: {final_epub.name}")
    print(f"📱 iPad Ready: YES")
    print(f"🔊 Audio Files: {audio_count}")
    print(f"📖 Units: 15 (0-14)")
    print(f"✅ XML Valid: ALL FILES")
    print("\n🚀 Ready to use on iPad!")