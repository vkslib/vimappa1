# PowerShell script to generate audio files for all units
Set-Location "d:\my code\mypadbookvim\mypadbookvim"

Write-Host "=== Generating audio for Units 7-9 ===" -ForegroundColor Green
python generate_audio_units7-14.py

Write-Host "`n=== Generating audio for Units 10-13 ===" -ForegroundColor Green  
python generate_audio_units10-14.py

Write-Host "`n=== All audio generation complete! ===" -ForegroundColor Cyan
Read-Host "Press Enter to exit"
