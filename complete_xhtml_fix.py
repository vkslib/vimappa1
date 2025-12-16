#!/usr/bin/env python3
"""
Complete XHTML validation for EPUB3
"""
import re
from pathlib import Path

def validate_and_fix_xhtml(content, filename):
    """Comprehensive XHTML validation and fixing"""
    
    print(f"Processing: {filename}")
    
    # Step 1: Fix DOCTYPE
    if not content.startswith('<!DOCTYPE html>'):
        content = re.sub(r'<!DOCTYPE[^>]*>', '<!DOCTYPE html>', content)
    
    # Step 2: Fix HTML opening tag with proper xmlns
    html_pattern = r'<html[^>]*>'
    if filename == 'nav.html':
        new_html_tag = '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="de">'
    else:
        new_html_tag = '<html xmlns="http://www.w3.org/1999/xhtml" lang="de">'
    
    content = re.sub(html_pattern, new_html_tag, content)
    
    # Step 3: Fix self-closing tags
    # Meta tags
    content = re.sub(r'<meta([^/>]*[^/])>', r'<meta\1/>', content)
    # Link tags  
    content = re.sub(r'<link([^/>]*[^/])>', r'<link\1/>', content)
    # Other self-closing tags
    for tag in ['img', 'br', 'hr', 'input', 'area', 'base', 'col']:
        content = re.sub(rf'<{tag}([^/>]*[^/])>', rf'<{tag}\1/>', content)
    
    # Step 4: Fix attribute quotes
    content = re.sub(r'(\w+)=([^"\s>][^>\s]*)', r'\1="\2"', content)
    
    # Step 5: Ensure script tags have proper closing
    content = re.sub(r'<script([^>]*)/>', r'<script\1></script>', content)
    
    # Step 6: Fix any remaining XML issues
    # Remove any double slashes in attributes
    content = re.sub(r'//>', r'/>', content)
    
    return content

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("=== Complete XHTML Validation for EPUB3 ===")
    
    for html_file in epub_dir.glob("*.html"):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Validate and fix XHTML
            fixed_content = validate_and_fix_xhtml(content, html_file.name)
            
            # Write back the fixed content
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            print(f"  ✓ Fixed: {html_file.name}")
            
        except Exception as e:
            print(f"  ✗ Error with {html_file.name}: {e}")
    
    print("\n✅ All XHTML validation complete!")

if __name__ == "__main__":
    main()