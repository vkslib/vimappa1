# Auto Git Push Script
# รันใน PowerShell: powershell -ExecutionPolicy Bypass -File auto-git.ps1

$watchPath = "."
$lastCommitTime = Get-Date

Write-Host "🔍 กำลังติดตาม files ในโฟลเดอร์: $watchPath"
Write-Host "📁 กด Ctrl+C เพื่อหยุด"

# สร้าง FileSystemWatcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $watchPath
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true
$watcher.Filter = "*.*"

# กรองไฟล์ที่ไม่ต้องการ
$excludePatterns = @("\.git", "node_modules", "\.log$", "\.tmp$")

# กำหนด Action สำหรับการเปลี่ยนแปลง
$action = {
    $path = $Event.SourceEventArgs.FullPath
    $changeType = $Event.SourceEventArgs.ChangeType
    
    # ตรวจสอบว่าไฟล์อยู่ในรายการที่ไม่ต้องการหรือไม่
    $shouldExclude = $false
    foreach ($pattern in $excludePatterns) {
        if ($path -match $pattern) {
            $shouldExclude = $true
            break
        }
    }
    
    if (-not $shouldExclude) {
        $currentTime = Get-Date
        $timeDiff = ($currentTime - $script:lastCommitTime).TotalMinutes
        
        if ($timeDiff -ge 2) {  # รอ 2 นาทีก่อน commit ใหม่
            Write-Host "📝 ตรวจพบการเปลี่ยนแปลง: $path"
            Write-Host "⏳ กำลังอัปโหลดไปยัง GitHub..."
            
            # Git commands
            git add .
            $commitMsg = "🔄 Auto-update $(Get-Date -Format 'dd/MM/yyyy HH:mm')"
            git commit -m $commitMsg
            git push origin main
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "✅ อัปโหลดสำเร็จ!"
                Write-Host "🌐 เว็บไซต์จะอัปเดตภายใน 1-2 นาที"
            } else {
                Write-Host "❌ เกิดข้อผิดพลาดในการอัปโหลด"
            }
            
            $script:lastCommitTime = $currentTime
        }
    }
}

# Register Events
Register-ObjectEvent -InputObject $watcher -EventName "Changed" -Action $action
Register-ObjectEvent -InputObject $watcher -EventName "Created" -Action $action
Register-ObjectEvent -InputObject $watcher -EventName "Deleted" -Action $action

# รอ input
try {
    while ($true) {
        Start-Sleep 1
    }
} finally {
    $watcher.Dispose()
    Write-Host "📴 หยุดติดตามไฟล์"
}