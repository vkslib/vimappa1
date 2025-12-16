# PowerShell script to check for missing audio files
Write-Host "🔍 กำลังตรวจสอบไฟล์เสียงที่หายไป..." -ForegroundColor Cyan

$chapterFiles = Get-ChildItem -Path "chapters" -Filter "*.html"
$missingFiles = @()

foreach ($file in $chapterFiles) {
    Write-Host "`n📄 ตรวจสอบ: $($file.Name)" -ForegroundColor Yellow
    
    $content = Get-Content $file.FullName -Raw
    
    # หา path ของไฟล์เสียงทั้งหมด
    $audioMatches = [regex]::Matches($content, "onclick=`"play\('\.\.\/audio\/([^']+)'\)")
    
    foreach ($match in $audioMatches) {
        $audioPath = $match.Groups[1].Value
        $fullPath = "audio\$audioPath"
        
        if (-not (Test-Path $fullPath)) {
            $missingFiles += @{
                Chapter = $file.Name
                AudioPath = $audioPath
                FullPath = $fullPath
            }
            Write-Host "❌ ไม่พบ: $audioPath" -ForegroundColor Red
        } else {
            Write-Host "✅ พบ: $audioPath" -ForegroundColor Green
        }
    }
}

Write-Host "`n📊 สรุปผลการตรวจสอบ:" -ForegroundColor Magenta
Write-Host "═══════════════════════════════" -ForegroundColor Magenta

if ($missingFiles.Count -eq 0) {
    Write-Host "🎉 ไฟล์เสียงครบทุกไฟล์!" -ForegroundColor Green
} else {
    Write-Host "⚠️  พบไฟล์เสียงที่หายไป $($missingFiles.Count) ไฟล์:" -ForegroundColor Red
    
    foreach ($missing in $missingFiles) {
        Write-Host "  📂 $($missing.Chapter): $($missing.AudioPath)" -ForegroundColor Yellow
    }
    
    Write-Host "`n🔧 แนะนำการแก้ไข:" -ForegroundColor Cyan
    Write-Host "1. สร้างไฟล์เสียงที่หายไปด้วย edge-tts" 
    Write-Host "2. หรือแก้ไข path ในไฟล์ HTML ให้ถูกต้อง"
    Write-Host "3. ตรวจสอบชื่อไฟล์ว่าตรงกับที่มีอยู่หรือไม่"
}

Write-Host "`n🎯 GitDoc จะ sync การแก้ไขอัตโนมัติ!" -ForegroundColor Green