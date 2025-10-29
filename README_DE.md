# AntiStutter 🎤

> **Wissenschaftlich fundierte Echtzeit-Stotterreduktion durch auditive Stimulation**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/DancingTedDanson011/antistutter)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-orange.svg)](LICENSE)
[![Research](https://img.shields.io/badge/research-peer--reviewed-success.svg)](#wissenschaftliche-grundlage)

[**English**](README.md) | [**Deutsch**](README_DE.md)

---

## 📋 Übersicht

Wissenschaftlich fundiertes Programm zur Reduktion von Stottern durch auditive Stimulation.

## Wissenschaftliche Grundlage

Basierend auf peer-reviewed Forschung:

- **Delayed Auditory Feedback (DAF)**: 30-70% Stotterreduktion
- **Frequency Altered Feedback (FAF)**: 30-60% Stotterreduktion
- **Rhythmische Stimulation**: Bis zu 100% Reduktion
- **Binaurale Beats**: ~25% Reduktion

### Quellen
- Antipova et al. (2008) - Journal of Fluency Disorders
- Kalinowski & Stuart (1996)
- Wiltshire et al. (2024) - PLoS ONE
- Chernetchenko et al. (2023) - Brain Sciences

## Installation

### Voraussetzungen

- Windows 10/11
- Python 3.10 oder neuer
- Mikrofon (eingebaut oder extern)
- **Kopfhörer oder Headset** (essentiell!)

### Schnellstart

1. **Python installieren** (falls noch nicht vorhanden):
   - Download: https://www.python.org/downloads/
   - ⚠️ **WICHTIG**: "Add Python to PATH" aktivieren!

2. **Programm starten**:
   - Doppelklick auf `start.bat`
   - Beim ersten Start werden automatisch alle Abhängigkeiten installiert (dauert 2-3 Minuten)

3. **Kopfhörer aufsetzen** und Mikrofon testen

4. **Preset auswählen**:
   - **Leicht**: Unauffällige Unterstützung
   - **Mittel**: Empfohlen für Alltag (Default)
   - **Stark**: Maximale Unterstützung

5. **START drücken** und sprechen!

## Bedienung

### Schnellstart-Presets

**Leicht**
- DAF: 50 ms Verzögerung
- FAF: -0,25 Oktaven
- Für leichte Fälle oder zum Ausprobieren

**Mittel** ⭐ Empfohlen
- DAF: 75 ms Verzögerung
- FAF: -0,5 Oktaven
- Binaurale Beats: Balanced
- Optimales Verhältnis Wirkung/Natürlichkeit

**Stark**
- DAF: 100 ms Verzögerung
- FAF: -0,5 Oktaven
- Metronom: 100 BPM
- Binaurale Beats: Fokussiert
- Für schwere Situationen

### Manuelle Anpassung (Custom)

#### Verzögertes Feedback (DAF)
- **Verzögerung**: 50-100 ms (empfohlen 75 ms)
- **Mix**: 70-90% (höher = mehr Effekt)
- Simuliert ein Echo der eigenen Stimme

#### Tonhöhen-Shift (FAF)
- **Shift**: -6 Halbtöne = halbe Oktave tiefer (empfohlen)
- **Mix**: 70-80%
- Simuliert "Chorsprechen" mit zweiter Person

#### Metronom
- **BPM**: 90-180 (120 empfohlen)
- **Lautstärke**: Nach Vorliebe
- Rhythmischer Klick zur Stabilisierung

#### Binaurale Beats
- **Entspannt**: Delta/Theta (Stressreduktion)
- **Balanced**: Delta/Theta/Beta Mix (empfohlen)
- **Fokussiert**: Theta/Beta (erhöhte Aufmerksamkeit)
- Wirkt auf Gehirnwellen-Ebene

## Technische Details

### Funktionsweise

1. **Mikrofon** nimmt deine Stimme auf
2. **Echtzeit-Verarbeitung** (Latenz <30 ms):
   - Verzögerung (Echo-Effekt)
   - Tonhöhenverschiebung (Chor-Effekt)
   - Metronom-Klicks addieren
   - Binaurale Beats mischen
3. **Kopfhörer** geben modifiziertes Audio aus
4. Dein **Gehirn** wird vom Stottern abgelenkt

### Latenz

- Typisch: 20-30 ms (unhörbar)
- Abhängig von Audio-Hardware
- Wird in der Statusleiste angezeigt

### System-Anforderungen

- **CPU**: Dual-Core 2 GHz+ (i3/Ryzen 3+)
- **RAM**: 4 GB (Programm nutzt ~200 MB)
- **Audio**: ASIO-Treiber empfohlen für niedrigste Latenz

## Häufige Probleme

### "Python nicht gefunden"
- Python installieren: https://www.python.org/downloads/
- Bei Installation "Add to PATH" aktivieren
- Computer neu starten

### "Audio-Gerät kann nicht geöffnet werden"
- Kopfhörer/Mikrofon anschließen vor Start
- In Windows-Soundeinstellungen Standard-Geräte prüfen
- Andere Audio-Programme schließen (Discord, Teams, etc.)

### "Rückkopplung / Echo"
⚠️ **NIE über Lautsprecher nutzen!** Immer Kopfhörer tragen!

### Verzögerung zu hoch / Roboter-Stimme
- Buffer-Größe in Config reduzieren (Fortgeschritten)
- Delay auf 50-75 ms reduzieren
- FAF-Mix reduzieren

### Kein Effekt spürbar
- Verschiedene Presets ausprobieren
- Lautstärke der Kopfhörer erhöhen
- DAF/FAF Mix erhöhen
- Individuell unterschiedlich - Geduld!

## Konfiguration

Einstellungen werden automatisch gespeichert in:
```
C:\Users\<Username>\.antistutter\config.json
```

Logs befinden sich in:
```
C:\Users\<Username>\.antistutter\logs\
```

## Deinstallation

1. Ordner `AntiStutter` löschen
2. Optional: `C:\Users\<Username>\.antistutter` löschen

## Entwicklung

### Projektstruktur

```
AntiStutter/
├── src/
│   ├── main.py              # Entry Point
│   ├── audio_engine.py      # Audio Processing
│   ├── dsp/                 # Signal Processing
│   │   ├── delay.py         # DAF
│   │   ├── pitch_shift.py   # FAF
│   │   ├── metronome.py     # Rhythmus
│   │   └── binaural.py      # Binaural Beats
│   ├── gui/                 # User Interface
│   └── utils/               # Config & Logging
├── assets/                  # Audio Files
├── tests/                   # Unit Tests
├── requirements.txt
├── start.bat
└── README.md
```

### Dependencies installieren

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Programm starten (Development)

```bash
python src/main.py
```

### Tests ausführen

```bash
pytest tests/
```

## Credits

Entwickelt basierend auf neurowissenschaftlicher Forschung zu auditiven Fluency-Inducing Conditions.

### Hauptreferenzen

1. Antipova, E. A., et al. (2008). "Effects of altered auditory feedback (AAF) on stuttering frequency during monologue speech production." *Journal of Fluency Disorders*, 33(4), 274-290.

2. Kalinowski, J., & Stuart, A. (1996). "Stuttering amelioration at various auditory feedback delays and speech rates." *European Journal of Disorders of Communication*, 31(3), 259-269.

3. Wiltshire, C. E., et al. (2024). "Speaking to a metronome reduces kinematic variability in typical speakers and people who stutter." *PLOS ONE*, 19(7).

4. Chernetchenko, D., et al. (2023). "Effects of Binaural Beat Stimulation in Adults with Stuttering." *Brain Sciences*, 13(2).

Vollständige Quellenangaben in den PDFs im Projektverzeichnis.

## 📜 Lizenz

Dieses Projekt ist lizenziert unter **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

### ✅ Erlaubt:
- Nutzung für **private**, **Bildungs-** und **Forschungszwecke**
- Code modifizieren und anpassen
- Mit Namensnennung teilen

### ❌ Nicht erlaubt:
- **Kommerzielle Nutzung** (bezahlte Dienste, kommerzielle Produkte)
- Verkauf der Software oder Derivate
- Nutzung in gewinnorientierten Unternehmen ohne Erlaubnis

**Für kommerzielle Lizenzen**, kontaktieren Sie: your-email@example.com

Siehe [LICENSE](LICENSE) Datei für vollständige Details.

---

**Medizinischer Hinweis**: Dieses Programm ersetzt keine professionelle logopädische Therapie. Bei anhaltendem oder schwerem Stottern konsultieren Sie einen Sprachtherapeuten.

## Support

Bei Fragen oder Problemen:
- GitHub Issues: [Link]
- Log-Dateien prüfen: `%USERPROFILE%\.antistutter\logs\`

---

**Version**: 1.0.0
**Letzte Aktualisierung**: 2025-10-29

*Viel Erfolg! 🎤*
