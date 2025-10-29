@echo off
title AntiStutter - Installation
color 0B
echo.
echo ========================================
echo    AntiStutter v1.0
echo    Installations-Assistent
echo ========================================
echo.

REM Admin check
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [INFO] Keine Admin-Rechte erkannt.
    echo        Installation wird als normaler Benutzer fortgesetzt.
    echo.
)

REM Step 1: Check Python
echo [1/5] Pruefe Python Installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [FEHLER] Python ist nicht installiert!
    echo.
    echo Bitte installiere Python 3.10 oder neuer:
    echo https://www.python.org/downloads/
    echo.
    echo WICHTIG beim Installieren:
    echo   [X] Add Python to PATH aktivieren!
    echo.
    echo Danach dieses Script nochmal ausfuehren.
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python %PYTHON_VERSION% gefunden!
echo.

REM Step 2: Check pip
echo [2/5] Pruefe pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo [INFO] pip nicht gefunden, installiere pip...
    python -m ensurepip --upgrade
)
echo [OK] pip verfuegbar!
echo.

REM Step 3: Create virtual environment
echo [3/5] Erstelle virtuelle Umgebung...
if exist "venv\" (
    echo [INFO] venv existiert bereits, wird neu erstellt...
    rmdir /s /q venv
)

python -m venv venv
if errorlevel 1 (
    echo [FEHLER] Konnte venv nicht erstellen!
    echo.
    echo Moeglicherweise fehlt das venv-Modul.
    echo Fuehre aus: python -m pip install virtualenv
    echo.
    pause
    exit /b 1
)
echo [OK] Virtuelle Umgebung erstellt!
echo.

REM Step 4: Activate and upgrade pip
echo [4/5] Aktiviere Umgebung und aktualisiere pip...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [FEHLER] Konnte venv nicht aktivieren!
    pause
    exit /b 1
)

python -m pip install --upgrade pip setuptools wheel
echo [OK] pip aktualisiert!
echo.

REM Step 5: Install dependencies
echo [5/5] Installiere Abhaengigkeiten...
echo Dies kann 3-5 Minuten dauern...
echo.

REM Install dependencies one by one for better error handling
echo  - numpy...
pip install numpy>=1.24.0
if errorlevel 1 (
    echo [WARNUNG] numpy Installation fehlgeschlagen!
)

echo  - scipy...
pip install scipy>=1.10.0
if errorlevel 1 (
    echo [WARNUNG] scipy Installation fehlgeschlagen!
)

echo  - sounddevice...
pip install sounddevice>=0.4.6
if errorlevel 1 (
    echo [WARNUNG] sounddevice Installation fehlgeschlagen!
)

echo  - soundfile...
pip install soundfile>=0.12.0
if errorlevel 1 (
    echo [WARNUNG] soundfile Installation fehlgeschlagen!
)

echo  - librosa...
pip install librosa>=0.10.0
if errorlevel 1 (
    echo [WARNUNG] librosa Installation fehlgeschlagen!
)

echo  - PyQt5...
pip install PyQt5>=5.15.0
if errorlevel 1 (
    echo [WARNUNG] PyQt5 Installation fehlgeschlagen!
)

echo.
echo [INFO] Verifikation der Installation...
python -c "import numpy, scipy, sounddevice, soundfile, librosa, PyQt5; print('[OK] Alle Module erfolgreich importiert!')" 2>nul
if errorlevel 1 (
    echo [WARNUNG] Einige Module konnten nicht importiert werden!
    echo.
    echo Pruefe die Fehler oben und versuche:
    echo   pip install -r requirements.txt --no-cache-dir
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo    Installation abgeschlossen!
echo ========================================
echo.
echo Naechste Schritte:
echo  1. Kopfhoerer anschliessen
echo  2. Doppelklick auf: start.bat
echo  3. Preset waehlen und START druecken
echo.
echo Dokumentation:
echo  - README.md        : Uebersicht
echo  - INSTALLATION.md  : Detaillierte Anleitung
echo  - USAGE.md         : Nutzungstipps
echo.
echo Bei Problemen:
echo  - test_audio_devices.bat (Audiogeraete testen)
echo  - run_tests.bat          (System-Tests)
echo.

REM Create desktop shortcut (optional)
set /p CREATE_SHORTCUT="Verknuepfung auf Desktop erstellen? (j/n): "
if /i "%CREATE_SHORTCUT%"=="j" (
    echo [INFO] Erstelle Desktop-Verknuepfung...
    set SCRIPT_DIR=%~dp0
    set DESKTOP=%USERPROFILE%\Desktop

    REM Create VBS script to make shortcut
    echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
    echo sLinkFile = "%DESKTOP%\AntiStutter.lnk" >> CreateShortcut.vbs
    echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
    echo oLink.TargetPath = "%SCRIPT_DIR%start.bat" >> CreateShortcut.vbs
    echo oLink.WorkingDirectory = "%SCRIPT_DIR%" >> CreateShortcut.vbs
    echo oLink.Description = "AntiStutter - Stotter-Reduktion" >> CreateShortcut.vbs
    echo oLink.Save >> CreateShortcut.vbs

    cscript //nologo CreateShortcut.vbs
    del CreateShortcut.vbs

    echo [OK] Verknuepfung erstellt!
)

echo.
echo Installation erfolgreich abgeschlossen!
echo.
deactivate
pause
