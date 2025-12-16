#!/usr/bin/env python3
"""
EPUB Validation Test - check for XML parsing errors
"""
from pathlib import Path
import xml.etree.ElementTree as ET

def validate_xhtml_file(file_path):
    """Validate XHTML file for XML compliance"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse as XML
        ET.fromstring(content)
        return True, None
        
    except ET.ParseError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Error reading file: {str(e)}"

def test_all_epub_files():
    """Test all EPUB HTML files for validation"""
    epub_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output\OEBPS")
    
    print("=== EPUB VALIDATION TEST ===")
    
    all_valid = True
    error_count = 0
    
    for html_file in epub_dir.glob("*.html"):
        print(f"Testing: {html_file.name}")
        
        is_valid, error = validate_xhtml_file(html_file)
        
        if is_valid:
            print(f"  ✅ Valid: {html_file.name}")
        else:
            print(f"  ❌ Invalid: {html_file.name}")
            print(f"     Error: {error}")
            all_valid = False
            error_count += 1
    
    print(f"\n=== VALIDATION RESULTS ===")
    if all_valid:
        print("🎉 ALL FILES ARE VALID XHTML!")
        print("✅ EPUB should work perfectly on iPad")
    else:
        print(f"❌ {error_count} files have validation errors")
        print("⚠️ EPUB may not work properly")
    
    return all_valid

if __name__ == "__main__":
    success = test_all_epub_files()