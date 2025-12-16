#!/usr/bin/env python3
"""
Check all audio paths in EPUB HTML files
"""
import re
from pathlib import Path
import os

def check_audio_paths():
    """Check all audio paths in HTML files and verify if files exist"""
    
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    audio_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\audio")
    
    print("=== CHECKING AUDIO PATHS ===")
    
    total_audio_buttons = 0
    missing_files = []
    found_files = []
    
    # Check each HTML file
    for html_file in sorted(epub_dir.glob("chapter*.html")):
        print(f"\nChecking: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all audio button paths
        audio_matches = re.findall(r"onclick=[\"']play\([\"']([^\"']+)[\"']\)[\"']", content)
        
        if not audio_matches:
            print(f"  ⚠️ No audio buttons found")
            continue
        
        print(f"  🔍 Found {len(audio_matches)} audio buttons")
        total_audio_buttons += len(audio_matches)
        
        for audio_path in audio_matches:
            # Convert relative path to absolute
            clean_path = audio_path.replace('../audio/', '')
            full_audio_path = audio_dir / clean_path
            
            if full_audio_path.exists():
                found_files.append(clean_path)
                print(f"    ✅ {clean_path}")
            else:
                missing_files.append(clean_path)
                print(f"    ❌ MISSING: {clean_path}")
    
    # Summary
    print(f"\n=== AUDIO CHECK SUMMARY ===")
    print(f"📊 Total audio buttons: {total_audio_buttons}")
    print(f"✅ Files found: {len(found_files)}")
    print(f"❌ Files missing: {len(missing_files)}")
    
    if missing_files:
        print(f"\n💥 MISSING FILES:")
        for missing in missing_files[:20]:  # Show first 20
            print(f"   - {missing}")
        if len(missing_files) > 20:
            print(f"   ... and {len(missing_files) - 20} more")
    
    # Check what audio files exist but aren't used
    existing_audio = []
    for category in ['vocab', 'sentences', 'dialogues']:
        cat_dir = audio_dir / category
        if cat_dir.exists():
            for mp3_file in cat_dir.glob("*.mp3"):
                existing_audio.append(f"{category}/{mp3_file.name}")
    
    unused_files = set(existing_audio) - set(found_files)
    if unused_files:
        print(f"\n📦 UNUSED AUDIO FILES: {len(unused_files)}")
        for unused in sorted(list(unused_files))[:10]:
            print(f"   - {unused}")
        if len(unused_files) > 10:
            print(f"   ... and {len(unused_files) - 10} more")
    
    return missing_files

if __name__ == "__main__":
    missing = check_audio_paths()
    if not missing:
        print("\n🎉 All audio files are properly linked!")
    else:
        print(f"\n⚠️ Need to fix {len(missing)} missing audio files")