@echo off
title AntiStutter - Starthilfe
color 0A
echo.
echo ========================================
echo    AntiStutter v1.0
echo    Wissenschaftlich fundierte
echo    Stotter-Reduktion
echo ========================================
echo.

REM Check Python Installation
echo [1/4] Pruefe Python Installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [FEHLER] Python nicht gefunden!
    echo.
    echo Bitte installiere Python 3.10 oder neuer von:
    echo https://www.python.org/downloads/
    echo.
    echo WICHTIG: Aktiviere "Add Python to PATH" bei der Installation!
    echo.
    pause
    exit /b 1
)

python --version
echo [OK] Python gefunden!
echo.

REM Check Virtual Environment
echo [2/4] Pruefe virtuelle Umgebung...
if not exist "venv\" (
    echo [INFO] Erstelle virtuelle Umgebung...
    python -m venv venv
    if errorlevel 1 (
        echo [FEHLER] Konnte venv nicht erstellen!
        pause
        exit /b 1
    )
    echo [OK] Virtuelle Umgebung erstellt!
)

REM Activate Virtual Environment
echo [INFO] Aktiviere virtuelle Umgebung...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [FEHLER] Konnte venv nicht aktivieren!
    pause
    exit /b 1
)
echo [OK] Virtuelle Umgebung aktiviert!
echo.

REM Install/Update Dependencies
echo [3/4] Pruefe Abhaengigkeiten...
pip show numpy >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installiere Abhaengigkeiten...
    echo Dies kann einige Minuten dauern...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [FEHLER] Installation fehlgeschlagen!
        echo.
        echo Moeglicherweise fehlen System-Bibliotheken.
        echo Fuer Windows empfehlen wir:
        echo - Microsoft Visual C++ Redistributable
        echo - PortAudio (kommt mit sounddevice)
        echo.
        pause
        exit /b 1
    )
    echo [OK] Abhaengigkeiten installiert!
) else (
    echo [OK] Abhaengigkeiten vorhanden!
)
echo.

REM Start Application
echo [4/4] Starte AntiStutter...
echo.
echo ========================================
echo  WICHTIG: Tragen Sie Kopfhoerer!
echo ========================================
echo.
timeout /t 2 /nobreak >nul

python src/main.py

REM Error Handling
if errorlevel 1 (
    echo.
    echo ========================================
    echo [FEHLER] Programmfehler aufgetreten!
    echo ========================================
    echo.
    echo Pruefe die Log-Datei fuer Details:
    echo %USERPROFILE%\.antistutter\logs\
    echo.
    pause
)

deactivate
