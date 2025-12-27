@echo off
REM ============================================================================
REM Car Bot Server - Auto-Start with Crash Recovery
REM This batch file runs the Flask server and automatically restarts on crash
REM ============================================================================

setlocal enabledelayedexpansion

:init
cd /d c:\Users\adeel\Trading2
title Car Bot Server [Running]
color 0A

:start_server
cls
echo ============================================================================
echo Car Bot Server - Auto-Restart Enabled
echo ============================================================================
echo.
echo Server starting at: %date% %time%
echo Status: RUNNING
echo URL: http://localhost:5000
echo.
echo Press CTRL+C to stop (not recommended - will lose availability)
echo.
echo ============================================================================
echo.

REM Activate virtual environment and run server
call venv\Scripts\activate.bat
python app.py

REM If we get here, the server crashed
echo.
echo ============================================================================
color 0C
echo ERROR: Server crashed at %date% %time%
echo Waiting 5 seconds before auto-restart...
echo ============================================================================
echo.
timeout /t 5 /nobreak

REM Loop back and restart
goto start_server

:end
pause
