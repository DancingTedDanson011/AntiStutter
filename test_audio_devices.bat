@echo off
title AntiStutter - Audio Geraete Test
echo.
echo ========================================
echo    Audio Geraete Test
echo ========================================
echo.

REM Activate venv if exists
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python -c "import sounddevice as sd; print('Verfuegbare Audio-Geraete:\n'); devices = sd.query_devices(); [print(f'{i}: {d[\"name\"]} (In: {d[\"max_input_channels\"]}, Out: {d[\"max_output_channels\"]})') for i, d in enumerate(devices)]"

echo.
echo ========================================
pause
