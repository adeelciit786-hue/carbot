# Create scheduled task - run this in PowerShell
$TaskName = "CarBotAutoStart"
$BatFile = "c:\Users\adeel\Trading2\start_server_forever.bat"

# Remove if exists
Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue | Out-Null
Start-Sleep -Milliseconds 500

# Create the scheduled task
$Action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$BatFile`""
$Trigger = New-ScheduledTaskTrigger -AtStartup
$Settings = New-ScheduledTaskSettingsSet -RunOnlyIfNetworkAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$Principal = New-ScheduledTaskPrincipal -RunLevel Highest -UserID "NT AUTHORITY\SYSTEM" -LogonType ServiceAccount

$Task = Register-ScheduledTask -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Principal $Principal `
    -Settings $Settings `
    -Description "Car Bot Server - Auto-starts on Windows boot with crash recovery" `
    -Force

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "✓ SUCCESS!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Your Car Bot server is now set up for auto-start:" -ForegroundColor Green
Write-Host ""
Write-Host "✓ Server will auto-start when Windows boots" -ForegroundColor Green
Write-Host "✓ Server will auto-restart if it crashes" -ForegroundColor Green
Write-Host "✓ Available at: http://localhost:5000" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Restart your computer to test" -ForegroundColor Cyan
Write-Host "2. Open http://localhost:5000 in your browser" -ForegroundColor Cyan
Write-Host "3. Server will be ready immediately!" -ForegroundColor Cyan
Write-Host ""
Write-Host "To check status anytime:" -ForegroundColor Yellow
Write-Host "  .\check_status.ps1" -ForegroundColor Yellow
Write-Host ""
Write-Host "To manually start now:" -ForegroundColor Yellow
Write-Host "  .\start_server_forever.bat" -ForegroundColor Yellow
Write-Host ""
