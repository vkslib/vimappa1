@echo off
cd /d "d:\my code\mypadbookvim\mypadbookvim"
echo === Generating audio for Units 7-9 ===
python generate_audio_units7-14.py
echo.
echo === Generating audio for Units 10-13 ===
python generate_audio_units10-14.py
echo.
echo === All audio generation complete! ===
pause
