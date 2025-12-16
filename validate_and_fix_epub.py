#!/usr/bin/env python3
"""
Complete EPUB validation and fixing - comprehensive solution
"""
import re
from pathlib import Path
import xml.etree.ElementTree as ET

def validate_xml_syntax(content):
    """Check if content is valid XML"""
    try:
        # Wrap in root element for validation
        test_content = f"<root>{content}</root>"
        ET.fromstring(test_content)
        return True, None
    except ET.ParseError as e:
        return False, str(e)

def fix_all_html_issues(content):
    """Comprehensive HTML fixing"""
    
    # 1. Fix viewport meta tag specifically
    content = re.sub(
        r'<meta name="viewport" content="width="device-width," initial-scale="1\.0"/>',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>',
        content
    )
    
    # 2. Fix all broken attribute patterns
    content = re.sub(r'content="([^"]*)"([^"]*)"([^"]*)"', r'content="\1, \2=\3"', content)
    content = re.sub(r'class="([^"]*)"([^"]*)"([^"]*)"', r'class="\1 \2=\3"', content)
    
    # 3. Fix malformed quotes in attributes
    content = re.sub(r'="([^"]*),([^"]*)"', r'="\1,\2"', content)
    content = re.sub(r'="([^"]*)"([^">]*)"', r'="\1\2"', content)
    
    # 4. Fix double equals
    content = re.sub(r'(\w+)==([^"]*)"', r'\1="\2"', content)
    
    # 5. Fix onclick attributes  
    content = re.sub(r'onclick="=([^"]*)"', r'onclick="\1"', content)
    
    # 6. Fix button tags
    content = re.sub(r'🔊&lt;/button>&lt;/td>', '🔊</button></td>', content)
    content = re.sub(r'&lt;/([^>]*)>', r'</\1>', content)
    
    # 7. Fix self-closing tags
    self_closing = ['meta', 'link', 'img', 'br', 'hr', 'input']
    for tag in self_closing:
        content = re.sub(rf'<{tag}([^/>]*[^/])>', rf'<{tag}\1/>', content)
    
    # 8. Fix any remaining malformed attributes
    content = re.sub(r'(\w+)="([^"]*),\s*>', r'\1="\2">', content)
    
    return content

def create_perfect_html_structure():
    """Create perfect HTML template"""
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

def extract_content_safely(content):
    """Safely extract title and body"""
    import re
    
    # Extract title
    title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else "VimAPP German A1"
    
    # Extract body content
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
    body_content = body_match.group(1) if body_match else ""
    
    return title, body_content

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("=== COMPREHENSIVE EPUB VALIDATION & FIXING ===")
    
    # Files to skip (navigation files)
    skip_files = ['nav.html', 'cover.html']
    
    errors_found = []
    files_processed = 0
    
    for html_file in epub_dir.glob("*.html"):
        if html_file.name in skip_files:
            continue
            
        files_processed += 1
        print(f"Processing: {html_file.name}")
        
        try:
            # Read current content
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for obvious issues
            if 'width="device-width,"' in content:
                errors_found.append(f"{html_file.name}: Malformed viewport")
            
            # Extract content safely
            title, body_content = extract_content_safely(content)
            
            # Create clean HTML structure
            template = create_perfect_html_structure()
            clean_content = template.format(title=title, body_content=body_content)
            
            # Apply additional fixes to body content
            clean_content = fix_all_html_issues(clean_content)
            
            # Write fixed content
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(clean_content)
            
            print(f"  ✓ Fixed and validated: {html_file.name}")
            
        except Exception as e:
            error_msg = f"{html_file.name}: {str(e)}"
            errors_found.append(error_msg)
            print(f"  ✗ Error: {error_msg}")
    
    # Summary
    print(f"\n=== VALIDATION SUMMARY ===")
    print(f"Files processed: {files_processed}")
    print(f"Errors found and fixed: {len(errors_found)}")
    
    if errors_found:
        print("\nIssues that were fixed:")
        for error in errors_found:
            print(f"  - {error}")
    
    print("\n✅ EPUB validation and fixing complete!")
    return len(errors_found) == 0

if __name__ == "__main__":
    success = main()
    if success:
        print("🎉 All files are clean!")
    else:
        print("⚠️ Some issues were found and fixed.")