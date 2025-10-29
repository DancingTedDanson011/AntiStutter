# AntiStutter - Installationsanleitung

## Schritt-für-Schritt Installation

### 1. Python installieren

1. Gehe zu https://www.python.org/downloads/
2. Lade die neueste Python 3.10+ Version für Windows herunter
3. **WICHTIG**: Starte den Installer
4. **AKTIVIERE** das Häkchen "Add Python to PATH" ✅
5. Klicke "Install Now"
6. Warte bis Installation abgeschlossen ist
7. Schließe den Installer

### 2. Python-Installation prüfen

1. Drücke `Windows + R`
2. Tippe `cmd` und drücke Enter
3. Tippe im schwarzen Fenster: `python --version`
4. Es sollte erscheinen: `Python 3.10.x` oder höher
5. Wenn Fehler: Computer neu starten und nochmal versuchen

### 3. AntiStutter starten

1. Navigiere zum AntiStutter-Ordner
2. **Doppelklick** auf `start.bat`
3. Beim ersten Start:
   - Es öffnet sich ein Kommandofenster
   - Automatische Installation der Abhängigkeiten (2-3 Minuten)
   - Es werden ~500 MB heruntergeladen
   - Warten bis "Starte AntiStutter..." erscheint
4. Das GUI-Fenster öffnet sich

### 4. Audio-Setup

1. **Kopfhörer** anschließen und aufsetzen
2. Prüfe Windows-Sound-Einstellungen:
   - Rechtsklick auf Lautsprecher-Symbol (Taskleiste)
   - "Soundeinstellungen öffnen"
   - **Eingabegerät**: Dein Mikrofon
   - **Ausgabegerät**: Deine Kopfhörer
3. Im AntiStutter:
   - Wähle Preset "Mittel"
   - Klicke "START"
   - Sprich etwas → Du solltest dich leicht verzögert und verändert hören

## Häufige Installations-Probleme

### Problem: "Python nicht gefunden"

**Lösung**:
1. Python nochmal installieren
2. UNBEDINGT "Add to PATH" aktivieren
3. Computer neu starten
4. `start.bat` nochmal ausführen

### Problem: "pip install schlägt fehl"

**Lösung**:
1. Internet-Verbindung prüfen
2. Firewall/Antivirus kurz deaktivieren
3. Als Administrator ausführen:
   - Rechtsklick auf `start.bat` → "Als Administrator ausführen"

### Problem: "Microsoft Visual C++ erforderlich"

**Lösung**:
1. Lade herunter: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Installiere Visual C++ Redistributable
3. Computer neu starten
4. `start.bat` nochmal ausführen

### Problem: "sounddevice/PyAudio Fehler"

**Lösung** (Erweitert):
```batch
REM Öffne CMD als Administrator
cd C:\Users\<Username>\Desktop\AntiStutter
venv\Scripts\activate
pip uninstall sounddevice soundfile
pip install sounddevice soundfile --no-cache-dir
```

### Problem: "PyQt5 import error"

**Lösung**:
```batch
venv\Scripts\activate
pip install PyQt5 --force-reinstall
```

## Manuelle Installation (für Fortgeschrittene)

```bash
# 1. Virtual Environment erstellen
python -m venv venv

# 2. Aktivieren
venv\Scripts\activate

# 3. Dependencies installieren
pip install --upgrade pip
pip install -r requirements.txt

# 4. Programm starten
python src/main.py
```

## Deinstallation

1. AntiStutter-Ordner löschen
2. Optional: `C:\Users\<Username>\.antistutter` löschen
3. Optional: Python deinstallieren (falls nicht für anderes benötigt)

## System-Anforderungen

### Minimum
- Windows 10 (64-bit)
- Intel Core i3 / AMD Ryzen 3
- 4 GB RAM
- 1 GB freier Speicherplatz
- Mikrofon (eingebaut oder USB)
- Kopfhörer oder Headset

### Empfohlen
- Windows 11 (64-bit)
- Intel Core i5 / AMD Ryzen 5 oder besser
- 8 GB RAM
- SSD mit 2 GB frei
- USB-Mikrofon (bessere Qualität)
- Studio-Kopfhörer oder Gaming-Headset

## Erste Schritte nach Installation

1. **Audio-Test**: In AntiStutter unten links sollte sich der grüne Balken bewegen wenn du sprichst
2. **Preset testen**: Probiere alle 3 Presets (Leicht, Mittel, Stark)
3. **Feintuning**: Passe die Regler an deine Vorlieben an
4. **Alltag**: Nutze das Programm täglich 10-30 Minuten

## Support

Bei Problemen:
1. Prüfe die Log-Datei: `%USERPROFILE%\.antistutter\logs\`
2. Führe aus: `test_audio_devices.bat` (zeigt verfügbare Geräte)
3. Führe aus: `run_tests.bat` (testet alle Komponenten)

## Nächste Schritte

- Lies die `README.md` für detaillierte Nutzung
- Sieh dir das `MVP_Dokument.md` für wissenschaftliche Details an
- Passe deine Einstellungen im Custom-Modus an

---

**Viel Erfolg!** 🎤
