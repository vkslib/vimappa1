#!/usr/bin/env python3
"""
Create final EPUB without copying over fixed files
"""
import os
import zipfile
from pathlib import Path

def create_epub_final():
    """Create the final EPUB file from existing OEBPS folder"""
    epub_output_dir = Path(r"d:\my code\mypadbookvim\mypadbookvim\epub_output")
    epub_file = Path(r"d:\my code\mypadbookvim\mypadbookvim\VimAPP_German_A1_Fixed.epub")
    
    # Remove existing epub file
    if epub_file.exists():
        epub_file.unlink()
    
    with zipfile.ZipFile(epub_file, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Add mimetype (uncompressed, first)
        epub.write(epub_output_dir / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
        
        # Add META-INF
        for file in (epub_output_dir / "META-INF").rglob("*"):
            if file.is_file():
                arcname = str(file.relative_to(epub_output_dir))
                epub.write(file, arcname)
        
        # Add OEBPS
        for file in (epub_output_dir / "OEBPS").rglob("*"):
            if file.is_file():
                arcname = str(file.relative_to(epub_output_dir))
                epub.write(file, arcname)
    
    return epub_file

if __name__ == "__main__":
    print("Creating final EPUB with fixed XHTML...")
    epub_file = create_epub_final()
    print(f"✅ Final EPUB created: {epub_file}")
    
    # Show file size
    size_mb = epub_file.stat().st_size / (1024 * 1024)
    print(f"📦 File size: {size_mb:.1f} MB")
    print("📱 Ready for iPad with proper XHTML!")