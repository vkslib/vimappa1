#!/usr/bin/env python3
"""
Clean and fix all HTML files properly
"""
import shutil
from pathlib import Path

def create_clean_html_template():
    """Create clean HTML template"""
    return '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="de">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title}</title>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>
{body_content}
</body>
</html>'''

def extract_body_and_title(content):
    """Extract body content and title from HTML"""
    import re
    
    # Extract title
    title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL | re.IGNORECASE)
    title = title_match.group(1) if title_match else "VimAPP German A1"
    
    # Extract body content
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    body_content = body_match.group(1) if body_match else content
    
    return title, body_content

def fix_html_file(file_path):
    """Fix HTML file by recreating with clean template"""
    print(f"Fixing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract content
    title, body_content = extract_body_and_title(content)
    
    # Create clean HTML
    template = create_clean_html_template()
    clean_html = template.format(title=title, body_content=body_content)
    
    # Write clean HTML
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(clean_html)

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("Creating clean HTML files for EPUB...")
    
    # Skip navigation files (they're special)
    skip_files = ['nav.html', 'cover.html']
    
    for html_file in epub_dir.glob("*.html"):
        if html_file.name in skip_files:
            continue
            
        try:
            fix_html_file(html_file)
            print(f"  ✓ Fixed: {html_file.name}")
        except Exception as e:
            print(f"  ✗ Error with {html_file.name}: {e}")
    
    print("✅ All HTML files cleaned!")

if __name__ == "__main__":
    main()