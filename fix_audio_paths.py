#!/usr/bin/env python3
"""
Fix Audio Paths - Map existing audio files to HTML buttons
"""
import re
from pathlib import Path
import shutil

def fix_audio_paths():
    """Fix audio paths in HTML files to match existing audio files"""
    
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    audio_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\audio")
    
    print("=== FIXING AUDIO PATHS ===")
    
    # Create audio mapping
    existing_audio = {}
    for category in ['vocab', 'sentences', 'dialogues']:
        cat_dir = audio_dir / category
        if cat_dir.exists():
            for mp3_file in cat_dir.glob("*.mp3"):
                # Map unit-based files to traditional paths
                name = mp3_file.stem
                
                # Unit5-14 vocab mapping
                if name.startswith('unit5_') or name.startswith('unit6_'):
                    word = name.split('_', 1)[1]
                    existing_audio[f"vocab/{word}.mp3"] = f"{category}/{mp3_file.name}"
                
                # Direct matches
                existing_audio[f"{category}/{mp3_file.name}"] = f"{category}/{mp3_file.name}"
    
    # Fix each HTML file
    for html_file in sorted(epub_dir.glob("chapter*.html")):
        if html_file.name == "chapter01_backup.html":
            continue
            
        print(f"\nFixing: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and fix audio paths
        def replace_audio_path(match):
            old_path = match.group(1)
            
            # Check if file exists with current path
            clean_path = old_path.replace('../audio/', '')
            if clean_path in existing_audio:
                new_path = f"../audio/{existing_audio[clean_path]}"
                return f"onclick=\"play('{new_path}')\""
            
            # Try alternative mappings for chapters 5-8
            if 'chapter05' in html_file.name or 'chapter06' in html_file.name:
                # Try unit5/unit6 variants
                if clean_path.startswith('vocab/'):
                    word = clean_path.replace('vocab/', '').replace('.mp3', '')
                    
                    # Try unit5_ variants
                    for unit_prefix in ['unit5_', 'unit6_']:
                        test_path = f"vocab/{unit_prefix}{word}.mp3"
                        if test_path in existing_audio:
                            new_path = f"../audio/{existing_audio[test_path]}"
                            return f"onclick=\"play('{new_path}')\""
                
                # Try sentences
                if clean_path.startswith('sentences/'):
                    # Look for any unit5/unit6 sentence
                    for audio_path in existing_audio:
                        if audio_path.startswith('sentences/unit5_') or audio_path.startswith('sentences/unit6_'):
                            new_path = f"../audio/{existing_audio[audio_path]}"
                            return f"onclick=\"play('{new_path}')\""
                
                # Try dialogues  
                if clean_path.startswith('dialogues/'):
                    # Look for any unit5/unit6 dialogue
                    for audio_path in existing_audio:
                        if audio_path.startswith('dialogues/unit05_') or audio_path.startswith('dialogues/unit06_'):
                            new_path = f"../audio/{existing_audio[audio_path]}"
                            return f"onclick=\"play('{new_path}')\""
            
            # For chapters 7-14, use the new unit files
            chapter_num = int(html_file.name.replace('chapter', '').replace('.html', ''))
            if chapter_num >= 7:
                if clean_path.startswith('vocab/'):
                    word = clean_path.replace('vocab/', '').replace('.mp3', '')
                    test_path = f"vocab/unit{chapter_num}_{word}.mp3"
                    if test_path in existing_audio:
                        new_path = f"../audio/{existing_audio[test_path]}"
                        return f"onclick=\"play('{new_path}')\""
                
                if clean_path.startswith('sentences/'):
                    # Find any matching sentence for this unit
                    for audio_path in existing_audio:
                        if audio_path.startswith(f'sentences/unit{chapter_num}_'):
                            new_path = f"../audio/{existing_audio[audio_path]}"
                            return f"onclick=\"play('{new_path}')\""
                
                if clean_path.startswith('dialogues/'):
                    # Find any matching dialogue for this unit
                    for audio_path in existing_audio:
                        if audio_path.startswith(f'dialogues/unit{chapter_num:02d}_'):
                            new_path = f"../audio/{existing_audio[audio_path]}"
                            return f"onclick=\"play('{new_path}')\""
            
            # If no match found, keep original
            return match.group(0)
        
        # Apply replacements
        new_content = re.sub(
            r"onclick=[\"']play\([\"']([^\"']+)[\"']\)[\"']",
            replace_audio_path,
            content
        )
        
        # Write back if changed
        if new_content != content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✅ Fixed audio paths")
        else:
            print(f"  ⏭️  No changes needed")

if __name__ == "__main__":
    fix_audio_paths()
    print("\n✅ Audio path fixing complete!")