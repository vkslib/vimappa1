#!/usr/bin/env python3
"""
ULTIMATE XML FIX - Fix all remaining mismatched tags systematically
"""
import re
from pathlib import Path
import xml.etree.ElementTree as ET

def fix_html_structure(content):
    """Fix HTML structure issues"""
    
    # Fix mismatched table headers
    content = re.sub(r'</th><tr>', '<tr>', content)
    content = re.sub(r'<tr>\s*</th>', '<tr>', content)
    
    # Fix unclosed tags
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Fix table structure issues
        if '</th><tr>' in line:
            line = line.replace('</th><tr>', '<tr>')
        if '<tr>' in line and '</th>' in line and '<th>' not in line:
            line = line.replace('</th>', '')
        
        # Fix mismatched strong/td tags
        if '</strong></td>' in line and '<td>' not in line:
            # This line likely starts with strong but no opening td
            line = re.sub(r'^(\s*)<strong>', r'\1<td><strong>', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_all_problematic_files():
    """Fix all files with XML validation errors"""
    
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    # Files that need fixing based on validation
    problematic_files = [
        'chapter00.html',
        'chapter01.html', 
        'chapter05.html',
        'chapter09.html',
        'chapter10.html',
        'chapter14.html',
        'nav.html'
    ]
    
    for filename in problematic_files:
        file_path = epub_dir / filename
        if not file_path.exists():
            continue
            
        print(f"Fixing structure: {filename}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply structural fixes
        fixed_content = fix_html_structure(content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"  ✅ Fixed structure: {filename}")

def create_perfect_nav():
    """Create perfect nav.html with proper EPUB namespace"""
    
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    nav_content = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="de">
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
    
    with open(epub_dir / "nav.html", 'w', encoding='utf-8') as f:
        f.write(nav_content)
    print("✅ Created perfect nav.html with proper namespace")

def validate_and_report():
    """Test validation and report results"""
    
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    valid_files = []
    invalid_files = []
    
    for html_file in sorted(epub_dir.glob("*.html")):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            ET.fromstring(content)
            valid_files.append(html_file.name)
            print(f"  ✅ Valid: {html_file.name}")
            
        except ET.ParseError as e:
            invalid_files.append((html_file.name, str(e)))
            print(f"  ❌ Invalid: {html_file.name}")
            print(f"     Error: {e}")
    
    print(f"\n=== VALIDATION SUMMARY ===")
    print(f"✅ Valid files: {len(valid_files)}")
    print(f"❌ Invalid files: {len(invalid_files)}")
    
    if len(invalid_files) == 0:
        print("\n🎉 ALL FILES ARE VALID!")
        return True
    else:
        print(f"\n⚠️ {len(invalid_files)} files still need fixing")
        return False

if __name__ == "__main__":
    print("=== ULTIMATE XML FIX ===")
    fix_all_problematic_files()
    create_perfect_nav()
    print("\n=== VALIDATION TEST ===")
    all_valid = validate_and_report()
    
    if all_valid:
        print("\n✅ EPUB is now perfect and ready!")
    else:
        print("\n⚠️ Some files still have issues")