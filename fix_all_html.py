#!/usr/bin/env python3
"""
Comprehensive HTML to XHTML conversion for EPUB3
"""
from pathlib import Path
import re

def fix_html_to_xhtml(content):
    """Convert HTML to valid XHTML for EPUB3"""
    
    # Fix DOCTYPE
    content = re.sub(r'<!DOCTYPE[^>]*>', '<!DOCTYPE html>', content)
    
    # Fix html opening tag
    content = re.sub(
        r'<html[^>]*>',
        '<html xmlns="http://www.w3.org/1999/xhtml" lang="de">',
        content
    )
    
    # Fix self-closing tags (must have closing slash in XHTML)
    self_closing_tags = ['meta', 'link', 'img', 'br', 'hr', 'input', 'area', 'base', 'col', 'embed', 'source', 'track', 'wbr']
    
    for tag in self_closing_tags:
        # Match tags that don't already end with />
        pattern = rf'<{tag}([^>]*[^/])>'
        replacement = rf'<{tag}\1/>'
        content = re.sub(pattern, replacement, content)
    
    # Fix attribute quotes (ensure all attributes are quoted)
    content = re.sub(r'(\w+)=([^"\s>]+)', r'\1="\2"', content)
    
    # Ensure script tags are properly closed
    content = re.sub(r'<script([^>]*)>\s*</script>', r'<script\1></script>', content)
    
    return content

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("Converting all HTML files to valid XHTML...")
    
    for html_file in epub_dir.glob("*.html"):
        if html_file.name in ['nav.html', 'cover.html']:
            continue  # Skip these as they're already correct
            
        print(f"Processing: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert to XHTML
        content = fix_html_to_xhtml(content)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print("✅ All HTML files converted to valid XHTML!")

if __name__ == "__main__":
    main()