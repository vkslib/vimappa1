#!/usr/bin/env python3
"""
Fix all malformed attributes in EPUB HTML files
"""
import re
from pathlib import Path

def fix_attributes_comprehensive(content):
    """Fix all types of malformed attributes"""
    
    # Fix double equals in class attributes
    content = re.sub(r'class==([^"]*)"', r'class="\1"', content)
    content = re.sub(r'id==([^"]*)"', r'id="\1"', content)
    content = re.sub(r'href==([^"]*)"', r'href="\1"', content)
    content = re.sub(r'src==([^"]*)"', r'src="\1"', content)
    
    # Fix missing closing quotes (followed by space or >)
    content = re.sub(r'class="([^"]*),\s*>', r'class="\1">', content)
    content = re.sub(r'id="([^"]*),\s*>', r'id="\1">', content)
    content = re.sub(r'href="([^"]*),\s*>', r'href="\1">', content)
    content = re.sub(r'src="([^"]*),\s*>', r'src="\1">', content)
    
    # Fix missing opening quotes
    content = re.sub(r'(\w+)=([^"\s>][^>\s]*)"', r'\1="\2"', content)
    
    # Fix any remaining unquoted attributes
    content = re.sub(r'(\w+)=([^"\s>]+)(\s|>)', r'\1="\2"\3', content)
    
    # Fix onclick attributes with unescaped characters
    content = re.sub(r"onclick='([^']*<[^']*)'", lambda m: f'onclick="{m.group(1).replace("<", "&lt;")}"', content)
    content = re.sub(r'onclick="([^"]*<[^"]*)"', lambda m: f'onclick="{m.group(1).replace("<", "&lt;")}"', content)
    
    # Escape any remaining < in attribute values
    content = re.sub(r'="([^"]*<[^"]*)"', lambda m: f'="{m.group(1).replace("<", "&lt;")}"', content)
    
    return content

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("Fixing all malformed attributes in EPUB files...")
    
    for html_file in epub_dir.glob("*.html"):
        print(f"Processing: {html_file.name}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix attributes
        fixed_content = fix_attributes_comprehensive(content)
        
        # Write fixed content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"  ✓ Fixed: {html_file.name}")
    
    print("✅ All attributes fixed!")

if __name__ == "__main__":
    main()