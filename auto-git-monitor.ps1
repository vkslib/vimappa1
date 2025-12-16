# Auto Git Monitor - ติดตามการเปลี่ยนแปลงไฟล์และ push อัตโนมัติ
# วิธีใช้: powershell -File "./auto-git-monitor.ps1"

Write-Host "🚀 VimAPP Auto Git Monitor เริ่มทำงาน"
Write-Host "📁 กำลังติดตาม: $(Get-Location)"
Write-Host "⏹️  กด Ctrl+C เพื่อหยุด"
Write-Host "=" * 50

$lastCommit = Get-Date

function Push-Changes {
    param($reason)
    
    Write-Host "🔄 $reason"
    Write-Host "📤 กำลังอัปโหลดไปยัง GitHub..."
    
    try {
        git add .
        $commitMessage = "🔄 Auto-update: $reason - $(Get-Date -Format 'HH:mm dd/MM/yyyy')"
        git commit -m $commitMessage
        git push origin main
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ อัปโหลดสำเร็จ!" -ForegroundColor Green
            Write-Host "🌐 เว็บไซต์จะอัปเดตใน 1-2 นาที" -ForegroundColor Cyan
            $script:lastCommit = Get-Date
        } else {
            Write-Host "❌ เกิดข้อผิดพลาด" -ForegroundColor Red
        }
    } catch {
        Write-Host "❌ Error: $_" -ForegroundColor Red
    }
    
    Write-Host "=" * 50
}

# ตัวอย่างการใช้งาน
Write-Host "💡 ตัวอย่างการใช้งาน:"
Write-Host "   1. แก้ไขไฟล์ใน VS Code"
Write-Host "   2. รันคำสั่ง: Push-Changes 'แก้ไข CSS'"
Write-Host "   3. หรือใช้ shortcut: git add . && git commit -m 'update' && git push"
Write-Host ""

# เก็บ session ไว้
while ($true) {
    Start-Sleep 10
    $changes = git status --porcelain
    if ($changes) {
        Write-Host "📝 ตรวจพบไฟล์ที่เปลี่ยนแปลง..." -ForegroundColor Yellow
        $timeDiff = (Get-Date) - $lastCommit
        if ($timeDiff.TotalMinutes -gt 5) {
            Push-Changes "ตรวจพบการเปลี่ยนแปลง"
        }
    }
}