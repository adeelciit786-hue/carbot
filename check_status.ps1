# ============================================================================
# Car Bot Server - Status Check
# Check if server is running and show details
# ============================================================================

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Car Bot Server - Status Check" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check if server is running
Write-Host "Checking server status..." -ForegroundColor Yellow

try {
    $response = Invoke-WebRequest -Uri "http://localhost:5000" -TimeoutSec 3 -ErrorAction Stop
    
    if ($response.StatusCode -eq 200) {
        Write-Host "✓ Server is RUNNING" -ForegroundColor Green
        Write-Host "  URL: http://localhost:5000" -ForegroundColor Green
        Write-Host "  Status Code: 200 OK" -ForegroundColor Green
        Write-Host ""
        
        # Check Python process
        $pythonProcess = Get-Process python -ErrorAction SilentlyContinue | Where-Object {$_.CommandLine -like "*app.py*"}
        if ($pythonProcess) {
            Write-Host "Process Details:" -ForegroundColor Cyan
            Write-Host "  PID: $($pythonProcess.Id)" -ForegroundColor Cyan
            Write-Host "  Name: $($pythonProcess.ProcessName)" -ForegroundColor Cyan
            Write-Host "  Memory: $([math]::Round($pythonProcess.WorkingSet64/1MB, 2)) MB" -ForegroundColor Cyan
        }
    }
}
catch {
    Write-Host "✗ Server is DOWN" -ForegroundColor Red
    Write-Host "  Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Start server with:" -ForegroundColor Yellow
    Write-Host "  1. Double-click: start_server_forever.bat" -ForegroundColor Yellow
    Write-Host "  2. Or run: .\restart_server.ps1" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Scheduled Task Status:" -ForegroundColor Cyan
$task = Get-ScheduledTask -TaskName "CarBotAutoStart" -ErrorAction SilentlyContinue
if ($task) {
    Write-Host "  Task: $($task.TaskName)" -ForegroundColor Cyan
    Write-Host "  State: $($task.State)" -ForegroundColor Cyan
} else {
    Write-Host "  Auto-start task not configured" -ForegroundColor Yellow
    Write-Host "  Setup with: .\setup_autostart.ps1" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
