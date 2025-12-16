#!/usr/bin/env python3
"""
Final comprehensive EPUB fix - manual approach
"""
from pathlib import Path

def create_perfect_chapter_header():
    """Create perfect XHTML header"""
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

def fix_file_manually(file_path, title):
    """Fix each file manually with perfect header"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract just the body content
    import re
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
    else:
        # If no body found, take content after <body>
        body_start = content.find('<body>')
        if body_start > -1:
            body_content = content[body_start + 6:]
            if '</body>' in body_content:
                body_content = body_content[:body_content.find('</body>')]
        else:
            body_content = content
    
    # Create perfect HTML
    template = create_perfect_chapter_header()
    perfect_html = template.format(title=title, body_content=body_content)
    
    # Write perfect HTML
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(perfect_html)

def main():
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    # Define titles for each chapter
    chapter_titles = {
        'chapter00.html': 'Unit 0: Das deutsche Alphabet',
        'chapter01.html': 'Unit 1: Personalpronomen',
        'chapter02.html': 'Unit 2: Familie',
        'chapter03.html': 'Unit 3: Beruf und Arbeit',
        'chapter04.html': 'Unit 4: Wohnung und Möbel',
        'chapter05.html': 'Unit 5: Essen und Trinken',
        'chapter06.html': 'Unit 6: Einkaufen und Zahlen',
        'chapter07.html': 'Unit 7: Freizeit und Hobbys',
        'chapter08.html': 'Unit 8: Gesundheit und Körper',
        'chapter09.html': 'Unit 9: Wetter und Jahreszeiten',
        'chapter10.html': 'Unit 10: Reisen und Verkehr',
        'chapter11.html': 'Unit 11: Schule und Lernen',
        'chapter12.html': 'Unit 12: Medien und Kommunikation',
        'chapter13.html': 'Unit 13: Kultur und Feste',
        'chapter14.html': 'Unit 14: Prüfungsvorbereitung',
        'table_of_contents.html': 'Table of Contents - VimAPP German A1'
    }
    
    print("=== MANUAL EPUB FIXING ===")
    
    for filename, title in chapter_titles.items():
        file_path = epub_dir / filename
        if file_path.exists():
            print(f"Fixing: {filename}")
            fix_file_manually(file_path, title)
            print(f"  ✓ Perfect: {filename}")
    
    print("\n✅ All files manually fixed with perfect XHTML structure!")

if __name__ == "__main__":
    main()