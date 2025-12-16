// Audio playback function with error handling
function play(src) {
  const audio = new Audio(src);
  
  audio.addEventListener('error', function(e) {
    console.error('Error loading audio file:', src);
    console.error('Error details:', e);
    // Show user-friendly message
    alert('ไฟล์เสียงยังไม่พร้อมใช้งาน\nAudio file not available yet: ' + src);
  });
  
  audio.addEventListener('canplay', function() {
    console.log('Audio file loaded successfully:', src);
  });
  
  audio.play().catch(function(error) {
    console.error('Playback error:', error);
  });
}

// Preload audio when page loads (optional)
document.addEventListener('DOMContentLoaded', function() {
  console.log('Page loaded. Audio system ready.');
});