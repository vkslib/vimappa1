#!/usr/bin/env python3
"""
Fix malformed attributes in EPUB HTML files
"""
import re
from pathlib import Path

def fix_malformed_attributes(content):
    """Fix malformed HTML attributes"""
    
    # Fix viewport meta tag with broken quotes
    content = re.sub(
        r'<meta name="viewport" content="width="device-width," initial-scale="1\.0"/">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>',
        content
    )
    
    # Fix any other malformed viewport tags
    content = re.sub(
        r'content="width="([^"]*)"[^"]*"([^"]*)"/"',
        r'content="width=\1, initial-scale=\2"',
        content
    )
    
    # Fix double quotes in attributes
    content = re.sub(r'="([^"]*)"([^"]*)"([^"]*)"', r'="\1, \2=\3"', content)
    
    # Fix charset attribute issues
    content = re.sub(r'charset="UTF-8"/', 'charset="UTF-8"', content)
    
    # Fix any remaining malformed attributes
    content = re.sub(r'(\w+)="([^"]*)"([^">]*)"([^">]*)"', r'\1="\2 \3=\4"', content)
    
    return content

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("Fixing malformed attributes in EPUB HTML files...")
    
    for html_file in epub_dir.glob("*.html"):
        print(f"Checking: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixed_content = fix_malformed_attributes(content)
        
        if fixed_content != original_content:
            print(f"  ✓ Fixed attributes in {html_file.name}")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
        else:
            print(f"  - No attribute issues in {html_file.name}")
    
    print("✅ All attribute issues fixed!")

if __name__ == "__main__":
    main()