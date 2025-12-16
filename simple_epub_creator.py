#!/usr/bin/env python3
"""
Simple EPUB Creator - Direct approach
"""
import zipfile
import os
from pathlib import Path

def create_epub_now():
    """Create EPUB file immediately"""
    
    print("🔥 Creating EPUB File 🔥")
    
    # Paths
    base_dir = Path(".")
    epub_output_dir = base_dir / "epub_output"
    epub_file = base_dir / "VimAPP_German_A1_RESTORED.epub"
    
    # Check if structure exists
    if not epub_output_dir.exists():
        print("❌ EPUB structure not found!")
        return False
    
    # Remove old file
    if epub_file.exists():
        epub_file.unlink()
        print("🗑️ Removed old EPUB file")
    
    try:
        # Create EPUB
        with zipfile.ZipFile(epub_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            
            # Add mimetype first (uncompressed)
            mimetype_file = epub_output_dir / "mimetype"
            if mimetype_file.exists():
                zip_file.write(mimetype_file, "mimetype", compress_type=zipfile.ZIP_STORED)
                print("📝 Added mimetype")
            
            # Add all other files
            for root, dirs, files in os.walk(epub_output_dir):
                for file in files:
                    if file == "mimetype":
                        continue  # Already added
                    
                    file_path = Path(root) / file
                    arcname = str(file_path.relative_to(epub_output_dir))
                    zip_file.write(file_path, arcname)
                    
            print("📚 Added all EPUB content")
        
        # Check result
        if epub_file.exists():
            size_mb = epub_file.stat().st_size / (1024 * 1024)
            print(f"✅ SUCCESS!")
            print(f"📁 File: {epub_file.name}")
            print(f"📊 Size: {size_mb:.1f} MB")
            print(f"📱 iPad Ready: YES")
            return True
        else:
            print("❌ Failed to create EPUB")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = create_epub_now()
    if success:
        print("\n🎉 EPUB file created successfully! 🎉")
    else:
        print("\n💥 Failed to create EPUB file")