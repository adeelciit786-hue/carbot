@echo off
REM Create scheduled task for auto-start
REM Run this once with admin privileges

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
"$TaskName = 'CarBotAutoStart'; " ^
"$ProjectPath = 'c:\Users\adeel\Trading2'; " ^
"$BatFile = '$ProjectPath\start_server_forever.bat'; " ^
"Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue; " ^
"$Action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument \"/c \"\"\`\"$BatFile\`\"\"\"; " ^
"$Trigger = New-ScheduledTaskTrigger -AtStartup; " ^
"$Settings = New-ScheduledTaskSettingsSet -RunOnlyIfNetworkAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries; " ^
"$Principal = New-ScheduledTaskPrincipal -RunLevel Highest -LogonType ServiceAccount -UserID 'SYSTEM'; " ^
"Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Principal $Principal -Settings $Settings -Description 'Car Bot Server'; " ^
"Write-Host 'SUCCESS: Task created - Server will auto-start on boot!' -ForegroundColor Green"

pause
