# AntiStutter - Projektübersicht

## 📋 Vollständige Dateistruktur

```
AntiStutter/
│
├── 📄 start.bat                    # Haupt-Startskript (HIER STARTEN!)
├── 📄 install.bat                  # Installations-Assistent
├── 📄 test_audio_devices.bat       # Audio-Geräte anzeigen
├── 📄 run_tests.bat                # System-Tests ausführen
│
├── 📖 README.md                    # Haupt-Dokumentation
├── 📖 INSTALLATION.md              # Installations-Anleitung
├── 📖 USAGE.md                     # Detaillierte Nutzungsanleitung
├── 📖 MVP_Dokument.md              # Wissenschaftliches MVP-Dokument
├── 📖 CHANGELOG.md                 # Versions-Historie
├── 📖 PROJECT_OVERVIEW.md          # Diese Datei
│
├── 📋 requirements.txt             # Python-Abhängigkeiten
├── 📋 .gitignore                   # Git-Ignorier-Regeln
│
├── 📁 src/                         # Quellcode
│   ├── __init__.py
│   ├── main.py                     # Entry Point
│   ├── audio_engine.py             # Audio-Verarbeitungs-Engine
│   │
│   ├── 📁 dsp/                     # Digital Signal Processing
│   │   ├── __init__.py
│   │   ├── delay.py                # DAF Implementation
│   │   ├── pitch_shift.py          # FAF Implementation
│   │   ├── metronome.py            # Metronom-Generator
│   │   └── binaural.py             # Binaurale Beats
│   │
│   ├── 📁 gui/                     # Grafische Oberfläche
│   │   ├── __init__.py
│   │   ├── main_window.py          # Hauptfenster
│   │   ├── widgets.py              # Custom Widgets
│   │   └── presets.py              # Preset-Manager
│   │
│   └── 📁 utils/                   # Hilfsfunktionen
│       ├── __init__.py
│       ├── config.py               # Konfigurations-Manager
│       └── logger.py               # Logging-System
│
├── 📁 assets/                      # Medien-Dateien
│   ├── 📁 sounds/                  # Metronom-Sounds
│   └── 📁 binaural_beats/          # Binaurale Beat Audio-Files
│
├── 📁 tests/                       # Test-Dateien
│   └── test_audio.py               # Audio-System Tests
│
├── 📁 dist/                        # Kompilierte Executables (später)
│
├── 📁 venv/                        # Virtuelle Python-Umgebung (wird erstellt)
│
└── 📑 Forschungs-PDFs              # Wissenschaftliche Quellen
    ├── Akustische Stimuli zur Reduzierung von Stottern.pdf
    └── Einführung_ Ablenkung als Mittel gegen Stottern.pdf
```

---

## 🚀 Schnellstart-Reihenfolge

### Für Endnutzer:

1. **`install.bat`** ausführen
   - Installiert Python-Dependencies
   - Richtet virtuelle Umgebung ein
   - Erstellt optional Desktop-Verknüpfung

2. **`start.bat`** ausführen
   - Startet das Programm
   - Kopfhörer aufsetzen!
   - Preset wählen → START

3. **Bei Problemen:**
   - `test_audio_devices.bat` → Audio-Geräte prüfen
   - `run_tests.bat` → System-Tests
   - `README.md` → Troubleshooting

### Für Entwickler:

1. `README.md` lesen
2. `MVP_Dokument.md` für wissenschaftlichen Hintergrund
3. Code in `src/` erkunden
4. Tests mit `run_tests.bat` ausführen

---

## 📊 Komponenten-Übersicht

### Core-Module

| Modul | Datei | Funktion | Wissenschaft |
|-------|-------|----------|--------------|
| **DAF** | `src/dsp/delay.py` | Verzögertes Audio-Feedback | 30-70% Reduktion (Kalinowski 1996) |
| **FAF** | `src/dsp/pitch_shift.py` | Tonhöhen-Verschiebung | 30-60% Reduktion (Antipova 2008) |
| **Metronom** | `src/dsp/metronome.py` | Rhythmische Stimulation | Bis 100% Reduktion (Wiltshire 2024) |
| **Binaural** | `src/dsp/binaural.py` | Gehirnwellen-Entrainment | ~25% Reduktion (Chernetchenko 2023) |

### Audio-Pipeline

```
[Mikrofon] → [Audio Engine] → [DSP Processing] → [Kopfhörer]
                    ↓
            ┌───────┴───────┐
            │  - DAF Delay  │
            │  - FAF Shift  │
            │  + Metronom   │
            │  + Binaural   │
            └───────────────┘
```

### GUI-Hierarchie

```
MainWindow (main_window.py)
├── PresetSelector (presets.py)
│   └── [Leicht] [Mittel] [Stark] [Custom]
├── ParameterGroups (widgets.py)
│   ├── DAF Controls (LabeledSlider)
│   ├── FAF Controls (LabeledSlider)
│   ├── Metronome Controls (LabeledSlider)
│   └── Binaural Controls (Buttons + Slider)
└── StatusBar
    └── LevelMeter (widgets.py)
```

---

## 🔧 Technische Details

### Audio-Spezifikationen

- **Sample Rate**: 44.1 kHz (CD-Qualität)
- **Buffer Size**: 1024 Samples (~23 ms)
- **Latenz**: <30 ms (typisch 20-25 ms)
- **Channels**: Mono Input → Stereo Output
- **Bitrate**: 32-bit Float

### DSP-Algorithmen

#### Delay Buffer (DAF)
```python
# Ringbuffer mit konfigurierbarer Größe
buffer_size = (delay_ms / 1000) * sample_rate
output[i] = buffer[read_pos]
buffer[write_pos] = input[i]
```

#### Pitch Shifting (FAF)
```python
# Resampling-basiert oder Phase Vocoder
ratio = 2^(semitones/12)
shifted = resample(audio, ratio)
```

#### Metronome
```python
# Sine wave mit Exponential Decay
frequency = 1000 Hz
click = sin(2π * frequency * t) * exp(-t * 100)
```

#### Binaural Beats
```python
# Frequenz-Differenz zwischen Ohren
left_freq = carrier
right_freq = carrier + beat_frequency
# Gehirn "hört" beat_frequency (z.B. 7 Hz)
```

---

## 📈 Performance-Metriken

### System-Anforderungen

| Komponente | Minimum | Empfohlen |
|------------|---------|-----------|
| **CPU** | Dual-Core 2 GHz | Quad-Core 2.5 GHz |
| **RAM** | 4 GB | 8 GB |
| **Speicher** | 1 GB | 2 GB SSD |
| **OS** | Windows 10 | Windows 11 |
| **Audio** | Onboard | USB/ASIO |

### Erwartete Performance

- **CPU-Last**: 5-15% (i5/Ryzen 5)
- **RAM-Nutzung**: 150-250 MB
- **Latenz**: 15-30 ms (Hardware-abhängig)
- **Startup-Zeit**: 2-5 Sekunden

---

## 🧪 Testing

### Automatische Tests

```bash
run_tests.bat
```

**Testet:**
- ✓ Delay Buffer Funktionalität
- ✓ Pitch Shifter Genauigkeit
- ✓ Metronome Timing
- ✓ Binaural Beat Generierung

### Manuelle Tests

1. **Audio-Geräte**: `test_audio_devices.bat`
2. **Mikrofon**: Grüner Balken bewegt sich?
3. **Kopfhörer**: Hörst du dich verzögert?
4. **Presets**: Alle 3 getestet?
5. **Latenz**: <50 ms in Statusleiste?

---

## 🐛 Troubleshooting

### Häufigste Probleme

| Problem | Datei prüfen | Lösung |
|---------|--------------|--------|
| Python nicht gefunden | - | `install.bat` ausführen |
| Modul-Import-Fehler | `requirements.txt` | `pip install -r requirements.txt` |
| Kein Audio | `config.json` | Standard-Geräte in Windows prüfen |
| Hohe Latenz | `config.json` → buffer_size | Auf 512 reduzieren |
| Rückkopplung | - | NUR Kopfhörer nutzen! |

### Log-Dateien

```
C:\Users\<Username>\.antistutter\logs\antistutter_YYYYMMDD.log
```

**Zeigt:**
- Startup-Sequenz
- Audio-Gerät-Initialisierung
- Fehler & Warnungen
- Performance-Metriken

---

## 📚 Dokumentation

### Für Nutzer

1. **README.md** - Start hier!
2. **INSTALLATION.md** - Schritt-für-Schritt Setup
3. **USAGE.md** - Tipps & Tricks für beste Ergebnisse

### Für Therapeuten/Forscher

4. **MVP_Dokument.md** - Wissenschaftliche Grundlagen
5. **Forschungs-PDFs** - Original-Studien
6. **CHANGELOG.md** - Was ist neu?

### Für Entwickler

7. **PROJECT_OVERVIEW.md** (diese Datei)
8. Code-Kommentare in `src/`
9. Docstrings in allen Modulen

---

## 🔮 Roadmap

### v1.1 (Geplant)
- [ ] Englische Übersetzung
- [ ] Preset-Speicherung
- [ ] Statistiken & Analytics
- [ ] Automatische Backup-Config

### v1.2 (Geplant)
- [ ] Mobile App (Android/iOS)
- [ ] Cloud-Sync
- [ ] Therapeuten-Dashboard

### v2.0 (Vision)
- [ ] Machine Learning Optimierung
- [ ] Echtzit-Stotter-Detektion
- [ ] Video-Call Integration (Zoom/Teams)

---

## 🤝 Mitwirken

### Code-Beiträge

1. Fork das Repository
2. Feature-Branch erstellen
3. Code schreiben & testen
4. Pull Request mit Beschreibung

### Wissenschaft-Beiträge

- Neue Studien → PDFs hinzufügen
- Parameter-Optimierung → Resultate teilen
- Klinische Daten → Anonymisiert beitragen

---

## 📄 Lizenz

Forschungs- und Bildungszwecke.

**Medizinischer Hinweis:**
Ersetzt keine professionelle Therapie.

---

## 📞 Support

- **Logs prüfen**: `%USERPROFILE%\.antistutter\logs\`
- **Tests ausführen**: `run_tests.bat`
- **Audio-Geräte**: `test_audio_devices.bat`
- **GitHub Issues**: [Link einfügen]

---

## ✅ Projekt-Status

**Version:** 1.0.0 MVP
**Status:** ✅ Produktionsbereit
**Letzte Aktualisierung:** 2025-10-29

### Komponenten-Status

| Komponente | Status | Tests |
|------------|--------|-------|
| Audio Engine | ✅ Fertig | ✅ Bestanden |
| DAF | ✅ Fertig | ✅ Bestanden |
| FAF | ✅ Fertig | ✅ Bestanden |
| Metronom | ✅ Fertig | ✅ Bestanden |
| Binaural Beats | ✅ Fertig | ✅ Bestanden |
| GUI | ✅ Fertig | ⏳ Manuell |
| Dokumentation | ✅ Fertig | - |

---

**Entwickelt mit ❤️ basierend auf neurowissenschaftlicher Forschung**

*Viel Erfolg beim Sprechen!* 🎤
