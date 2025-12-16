#!/usr/bin/env python3
"""
Complete HTML cleanup for EPUB
"""
import re
from pathlib import Path

def clean_html_completely(content):
    """Clean HTML completely and properly"""
    
    # Step 1: Fix malformed button tags
    content = re.sub(r'🔊&lt;/button>&lt;/td>', '🔊</button></td>', content)
    content = re.sub(r'&lt;/button>&lt;/td>', '</button></td>', content)
    
    # Step 2: Fix button attributes
    content = re.sub(r'<button class="audio-btn,\s*onclick="=([^"]*)">', r'<button class="audio-btn" onclick="\1">', content)
    content = re.sub(r'<button class="audio-btn" onclick="([^"]*),\s*>', r'<button class="audio-btn" onclick="\1">', content)
    
    # Step 3: Fix all malformed class attributes
    content = re.sub(r'class="([^"]*),\s*', r'class="\1"', content)
    content = re.sub(r'class==([^"]*)"', r'class="\1"', content)
    
    # Step 4: Fix onclick attributes
    content = re.sub(r'onclick="=([^"]*)"', r'onclick="\1"', content)
    
    # Step 5: Fix any remaining malformed tags
    content = re.sub(r'(\w+)="([^"]*),\s*>', r'\1="\2">', content)
    
    return content

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("Complete HTML cleanup for EPUB...")
    
    for html_file in epub_dir.glob("*.html"):
        print(f"Cleaning: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean HTML
        cleaned_content = clean_html_completely(content)
        
        # Write cleaned content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"  ✓ Cleaned: {html_file.name}")
    
    print("✅ All HTML cleaned!")

if __name__ == "__main__":
    main()