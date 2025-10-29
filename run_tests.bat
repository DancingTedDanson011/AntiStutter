@echo off
title AntiStutter - Tests
echo.
echo ========================================
echo    AntiStutter Tests
echo ========================================
echo.

REM Activate venv
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo [FEHLER] Virtuelle Umgebung nicht gefunden!
    echo Bitte erst start.bat ausfuehren.
    pause
    exit /b 1
)

echo Running tests...
echo.

python tests/test_audio.py

echo.
pause
