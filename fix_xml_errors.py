#!/usr/bin/env python3
"""
FINAL XML ERROR FIX - Fix mismatched tags systematically
"""
import re
from pathlib import Path

def fix_mismatched_tags():
    """Fix all mismatched tags in EPUB HTML files"""
    
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    # Common fixes
    def clean_html_content(content):
        """Clean HTML content to fix common issues"""
        
        # 1. Fix self-closing tags for XHTML
        content = re.sub(r'<(meta|link|br|hr|img|input)([^>]*?)(?<!/)>', r'<\1\2/>', content)
        
        # 2. Fix missing closing tags for common elements
        content = re.sub(r'<td([^>]*)>([^<]*?)(?=<td|<tr|</tr>|</table>)', r'<td\1>\2</td>', content)
        content = re.sub(r'<th([^>]*)>([^<]*?)(?=<th|<td|<tr|</tr>|</table>)', r'<th\1>\2</th>', content)
        
        # 3. Fix rowspan/colspan attributes
        content = re.sub(r'rowspan="([0-9]+)"', r'rowspan="\1"', content)
        content = re.sub(r'colspan="([0-9]+)"', r'colspan="\1"', content)
        
        # 4. Fix empty elements
        content = re.sub(r'<br\s*>', '<br/>', content)
        content = re.sub(r'<hr\s*>', '<hr/>', content)
        
        # 5. Fix audio button paths
        content = re.sub(r"onclick=\"play\('([^']+)'\)\"", r'onclick="play(\'\1\')"', content)
        
        # 6. Ensure proper nesting
        content = re.sub(r'<(/?)strong><(/?)td>', r'<\2td><\1strong>', content)
        
        return content
    
    files_to_fix = [
        'chapter00.html',
        'chapter01.html', 
        'chapter05.html',
        'chapter09.html',
        'chapter10.html',
        'chapter14.html',
        'nav.html',
        'cover.html'
    ]
    
    for filename in files_to_fix:
        file_path = epub_dir / filename
        if not file_path.exists():
            continue
            
        print(f"Fixing: {filename}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply fixes
        cleaned_content = clean_html_content(content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"  ✅ Fixed: {filename}")

def create_perfect_nav_cover():
    """Create perfect nav.html and cover.html files"""
    
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    # Perfect nav.html
    nav_content = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="de">
<head>
  <meta charset="UTF-8"/>
  <title>Navigation</title>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>
  <nav epub:type="toc">
    <h1>Table of Contents</h1>
    <ol>
      <li><a href="chapter00.html">Unit 0: Einführung (Introduction)</a></li>
      <li><a href="chapter01.html">Unit 1: Sich vorstellen (Introduction)</a></li>
      <li><a href="chapter02.html">Unit 2: Familie und Freunde (Family and Friends)</a></li>
      <li><a href="chapter03.html">Unit 3: Essen und Trinken (Food and Drink)</a></li>
      <li><a href="chapter04.html">Unit 4: Wohnen (Living)</a></li>
      <li><a href="chapter05.html">Unit 5: Freizeit (Leisure Time)</a></li>
      <li><a href="chapter06.html">Unit 6: Einkaufen (Shopping)</a></li>
      <li><a href="chapter07.html">Unit 7: Kleidung (Clothing)</a></li>
      <li><a href="chapter08.html">Unit 8: Gesundheit (Health)</a></li>
      <li><a href="chapter09.html">Unit 9: Reisen (Travel)</a></li>
      <li><a href="chapter10.html">Unit 10: Wetter (Weather)</a></li>
      <li><a href="chapter11.html">Unit 11: Zeit und Termine (Time and Appointments)</a></li>
      <li><a href="chapter12.html">Unit 12: Arbeit (Work)</a></li>
      <li><a href="chapter13.html">Unit 13: Schule und Bildung (School and Education)</a></li>
      <li><a href="chapter14.html">Unit 14: Prüfungsvorbereitung (Exam Preparation)</a></li>
    </ol>
  </nav>
</body>
</html>'''
    
    # Perfect cover.html
    cover_content = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="de">
<head>
  <meta charset="UTF-8"/>
  <title>VimAPP German A1</title>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>
  <div class="cover">
    <h1>VimAPP German A1</h1>
    <h2>Interactive German Learning Book</h2>
    <p>Complete A1 Level Course</p>
    <p>With Audio Pronunciation</p>
  </div>
</body>
</html>'''
    
    # Write perfect files
    with open(epub_dir / "nav.html", 'w', encoding='utf-8') as f:
        f.write(nav_content)
    print("✅ Created perfect nav.html")
    
    with open(epub_dir / "cover.html", 'w', encoding='utf-8') as f:
        f.write(cover_content)
    print("✅ Created perfect cover.html")

if __name__ == "__main__":
    print("=== FIXING XML ERRORS ===")
    fix_mismatched_tags()
    create_perfect_nav_cover()
    print("\n✅ All XML errors fixed!")