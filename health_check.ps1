# ============================================================================
# Car Bot Server - Health Check & Auto-Restart
# Checks if server is running every 2 minutes, restarts if needed
# ============================================================================

param(
    [int]$CheckIntervalSeconds = 120,
    [string]$ServerUrl = "http://localhost:5000",
    [string]$ProjectPath = "c:\Users\adeel\Trading2"
)

function Test-ServerHealth {
    try {
        $response = Invoke-WebRequest -Uri $ServerUrl -TimeoutSec 3 -ErrorAction Stop
        return $response.StatusCode -eq 200
    }
    catch {
        return $false
    }
}

function Start-CarBotServer {
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Starting Car Bot Server..." -ForegroundColor Green
    
    $scriptBlock = {
        cd $using:ProjectPath
        & ".\venv\Scripts\activate.ps1"
        python app.py
    }
    
    Start-Job -ScriptBlock $scriptBlock -Name "CarBotServer" | Out-Null
    Start-Sleep -Seconds 3
}

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Car Bot Server - Health Check Monitor" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Checking every $CheckIntervalSeconds seconds" -ForegroundColor Yellow
Write-Host "URL: $ServerUrl" -ForegroundColor Yellow
Write-Host "Press CTRL+C to stop monitoring" -ForegroundColor Yellow
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

$restartCount = 0

while ($true) {
    $isHealthy = Test-ServerHealth
    
    if ($isHealthy) {
        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] ✓ Server is HEALTHY" -ForegroundColor Green
    }
    else {
        $restartCount++
        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] ✗ Server is DOWN - Auto-restarting (#$restartCount)..." -ForegroundColor Red
        
        # Kill any existing Python processes
        Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force
        Start-Sleep -Seconds 2
        
        # Start server
        Start-CarBotServer
    }
    
    # Wait for next check
    Start-Sleep -Seconds $CheckIntervalSeconds
}
