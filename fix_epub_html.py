#!/usr/bin/env python3
"""
Fix HTML syntax errors for EPUB3 compatibility
"""
import re
from pathlib import Path

def fix_html_file(file_path):
    """Fix HTML syntax for EPUB3/XHTML compatibility"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Fixing: {file_path.name}")
    
    # Fix DOCTYPE
    content = re.sub(r'<!DOCTYPE[^>]*>', '<!DOCTYPE html>', content)
    
    # Fix html tag
    content = re.sub(
        r'<html[^>]*>',
        '<html xmlns="http://www.w3.org/1999/xhtml" lang="de">',
        content
    )
    
    # Fix self-closing tags - add closing slash
    content = re.sub(r'<meta([^>]*[^/])>', r'<meta\1/>', content)
    content = re.sub(r'<link([^>]*[^/])>', r'<link\1/>', content)
    content = re.sub(r'<img([^>]*[^/])>', r'<img\1/>', content)
    content = re.sub(r'<br([^>]*[^/])>', r'<br\1/>', content)
    content = re.sub(r'<hr([^>]*[^/])>', r'<hr\1/>', content)
    content = re.sub(r'<input([^>]*[^/])>', r'<input\1/>', content)
    
    # Fix double slashes
    content = re.sub(r'//', '/', content)
    content = content.replace('<meta/>', '<meta/>')
    
    # Fix script tags - ensure they have closing tags
    content = re.sub(r'<script([^>]*)></script>', r'<script\1></script>', content)
    content = re.sub(r'<script([^>]*)>', r'<script\1></script>', content)
    
    # Ensure all tags are properly closed
    # Fix any remaining unclosed tags
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("Fixing HTML syntax errors for EPUB3...")
    
    # Fix all HTML files
    for html_file in epub_dir.glob("*.html"):
        try:
            fix_html_file(html_file)
        except Exception as e:
            print(f"Error fixing {html_file.name}: {e}")
    
    print("✅ HTML files fixed!")

if __name__ == "__main__":
    main()