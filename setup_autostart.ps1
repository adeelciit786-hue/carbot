# ============================================================================
# Car Bot Server - Windows Task Scheduler Auto-Start Setup
# Run this ONCE to enable auto-start on Windows boot
# ============================================================================

param(
    [switch]$RemoveOnly = $false
)

$TaskName = "CarBotAutoStart"
$ProjectPath = "c:\Users\adeel\Trading2"
$BatFile = "$ProjectPath\start_server_forever.bat"

if ($RemoveOnly) {
    Write-Host "Removing existing scheduled task..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "✓ Task removed" -ForegroundColor Green
    exit
}

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Car Bot Auto-Start Setup" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Remove old task if exists
Write-Host "Removing old task if exists..." -ForegroundColor Yellow
Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue

# Create new task
Write-Host "Creating new scheduled task..." -ForegroundColor Yellow

$Action = New-ScheduledTaskAction `
    -Execute "cmd.exe" `
    -Argument "/c `"$BatFile`"" `
    -WorkingDirectory $ProjectPath

$Trigger = New-ScheduledTaskTrigger -AtStartup
$Settings = New-ScheduledTaskSettingsSet `
    -RunOnlyIfNetworkAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -Compatibility Win8

$Principal = New-ScheduledTaskPrincipal `
    -RunLevel Highest `
    -LogonType ServiceAccount `
    -UserID "SYSTEM"

$Task = Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Principal $Principal `
    -Settings $Settings `
    -Description "Car Bot Flask Server - Auto-starts on Windows boot with auto-restart on crash"

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "✓ Setup Complete!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "The Car Bot server will now:" -ForegroundColor Green
Write-Host "  • Auto-start whenever Windows boots" -ForegroundColor Green
Write-Host "  • Auto-restart if it crashes" -ForegroundColor Green
Write-Host "  • Be available at http://localhost:5000" -ForegroundColor Green
Write-Host ""
Write-Host "To verify it's working:" -ForegroundColor Cyan
Write-Host "  1. Restart your computer" -ForegroundColor Cyan
Write-Host "  2. Open http://localhost:5000 in browser" -ForegroundColor Cyan
Write-Host "  3. It should be ready immediately" -ForegroundColor Cyan
Write-Host ""
Write-Host "To check task status:" -ForegroundColor Cyan
Write-Host "  Get-ScheduledTask -TaskName $TaskName | Select-Object -Property State,Triggers" -ForegroundColor Cyan
Write-Host ""
Write-Host "To remove auto-start (if needed):" -ForegroundColor Cyan
Write-Host "  .\setup_autostart.ps1 -RemoveOnly" -ForegroundColor Cyan
Write-Host ""
