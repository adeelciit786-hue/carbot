# 🚗 CAR POSTING BOT - SERVER RESTART SCRIPT
# Use this whenever you need to restart the server after code changes

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  🚗 CAR POSTING BOT - RESTART SERVER                        ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Kill existing Python processes
Write-Host "⏹️  Stopping old server..." -ForegroundColor Yellow
taskkill /F /IM python.exe 2>$null | Out-Null
Start-Sleep -Seconds 2
Write-Host "✅ Done" -ForegroundColor Green
Write-Host ""

# Start new server
Write-Host "🚀 Starting fresh server..." -ForegroundColor Green
Write-Host "📍 Open: http://localhost:5000" -ForegroundColor Cyan
Write-Host "📝 Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

cd "c:\Users\adeel\Trading2"
python app.py

Write-Host ""
Write-Host "✋ Server stopped" -ForegroundColor Yellow
Write-Host ""
