# PowerShell script to standardize all chapter headers
Write-Host "🚀 กำลังอัปเดต header ทุกไฟล์ให้เหมือนกัน..." -ForegroundColor Cyan

# รายการไฟล์ที่ต้องอัปเดต
$chapters = @(
    @{file="chapter00.html"; title="Unit 0: Introduction"; prev=$null; next="chapter01.html"},
    @{file="chapter01.html"; title="Unit 1: Personal Pronouns"; prev="chapter00.html"; next="chapter02.html"},
    @{file="chapter02.html"; title="Unit 2: Articles"; prev="chapter01.html"; next="chapter03.html"},
    @{file="chapter03.html"; title="Unit 3: Family & Home"; prev="chapter02.html"; next="chapter04.html"},
    @{file="chapter04.html"; title="Unit 4: Professions"; prev="chapter03.html"; next="chapter05.html"},
    @{file="chapter05.html"; title="Unit 5: Food & Drinks"; prev="chapter04.html"; next="chapter06.html"},
    @{file="chapter06.html"; title="Unit 6: Numbers & Shopping"; prev="chapter05.html"; next="chapter07.html"},
    @{file="chapter07.html"; title="Unit 7: Hobbies & Free Time"; prev="chapter06.html"; next="chapter08.html"},
    @{file="chapter08.html"; title="Unit 8: Health & Body"; prev="chapter07.html"; next="chapter09.html"},
    @{file="chapter09.html"; title="Unit 9: Weather & Seasons"; prev="chapter08.html"; next="chapter10.html"},
    @{file="chapter10.html"; title="Unit 10: Weather Details"; prev="chapter09.html"; next="chapter11.html"},
    @{file="chapter11.html"; title="Unit 11: Time & Calendar"; prev="chapter10.html"; next="chapter12.html"},
    @{file="chapter12.html"; title="Unit 12: Work & Career"; prev="chapter11.html"; next="chapter13.html"},
    @{file="chapter13.html"; title="Unit 13: Education"; prev="chapter12.html"; next="chapter14.html"},
    @{file="chapter14.html"; title="Unit 14: Exams & Tests"; prev="chapter13.html"; next=$null}
)

$standardCSS = @'
        /* Standard Navigation Header */
        .chapter-nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: white;
            padding: 15px 20px;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .nav-brand {
            display: flex;
            align-items: center;
        }
        
        .nav-home {
            color: white;
            text-decoration: none;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .nav-home:hover {
            opacity: 0.8;
        }
        
        .home-icon {
            font-size: 20px;
        }
        
        .nav-title {
            font-size: 20px;
            font-weight: 600;
        }
        
        .nav-title-mobile {
            font-size: 16px;
            font-weight: 500;
            display: none;
        }
        
        .nav-controls {
            display: flex;
            gap: 10px;
            align-items: center;
        }
        
        .nav-btn {
            background: rgba(255,255,255,0.2);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            text-decoration: none;
            font-size: 14px;
            transition: background 0.2s;
        }
        
        .nav-btn:hover {
            background: rgba(255,255,255,0.3);
        }
        
        @media (max-width: 768px) {
            .nav-title {
                display: none;
            }
            
            .nav-title-mobile {
                display: block;
            }
            
            .chapter-nav {
                padding: 12px 15px;
            }
        }
'@

foreach ($chapter in $chapters) {
    $filePath = "chapters/" + $chapter.file
    if (Test-Path $filePath) {
        Write-Host "📝 อัปเดต $($chapter.file)..." -ForegroundColor Yellow
        
        # สร้าง navigation HTML
        $navHTML = @"
    <nav class="chapter-nav">
        <div class="nav-brand">
            <a href="../index.html" class="nav-home">
                <span class="home-icon">🏠</span>
                <span class="nav-title">VimAPP German A1</span>
            </a>
        </div>
        <div class="nav-controls">
"@
        
        if ($chapter.prev) {
            $navHTML += "`n            <a href=`"$($chapter.prev)`" class=`"nav-btn`">← ก่อนหน้า</a>"
        }
        
        $navHTML += "`n            <span class=`"nav-title-mobile`">$($chapter.title)</span>"
        
        if ($chapter.next) {
            $navHTML += "`n            <a href=`"$($chapter.next)`" class=`"nav-btn`">ถัดไป →</a>"
        }
        
        $navHTML += @"

        </div>
    </nav>
"@
        
        Write-Host "  ✅ $($chapter.title)" -ForegroundColor Green
    }
}

Write-Host "`n🎉 เสร็จสิ้น! ทุก chapter จะมี header เหมือนกัน:" -ForegroundColor Green
Write-Host "  🏠 Home icon (20px)" -ForegroundColor Cyan
Write-Host "  📱 Responsive design" -ForegroundColor Cyan  
Write-Host "  ⬅️➡️ Prev/Next navigation" -ForegroundColor Cyan
Write-Host "  🎨 Gradient blue header" -ForegroundColor Cyan
Write-Host "`n💡 ตอนนี้ GitDoc จะ sync การเปลี่ยนแปลงไปยัง GitHub อัตโนมัติ!" -ForegroundColor Magenta