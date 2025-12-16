#!/usr/bin/env python3
"""
Fix all xmlns URLs in EPUB HTML files
"""
from pathlib import Path
import re

def fix_xmlns_urls(content):
    """Fix malformed xmlns URLs"""
    # Fix missing slash in http://
    content = re.sub(r'xmlns="http:/www\.w3\.org', 'xmlns="http://www.w3.org', content)
    content = re.sub(r'xmlns:epub="http:/www\.idpf\.org', 'xmlns:epub="http://www.idpf.org', content)
    
    return content

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("Fixing xmlns URLs in all EPUB HTML files...")
    
    for html_file in epub_dir.glob("*.html"):
        print(f"Checking: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        fixed_content = fix_xmlns_urls(original_content)
        
        if fixed_content != original_content:
            print(f"  ✓ Fixed xmlns in {html_file.name}")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
        else:
            print(f"  - No changes needed for {html_file.name}")
    
    print("✅ All xmlns URLs fixed!")

if __name__ == "__main__":
    main()