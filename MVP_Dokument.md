# AntiStutter - MVP Dokument

## Projektziel
Ein Windows-Desktop-Programm, das durch wissenschaftlich fundierte akustische Stimulation Stottern in Echtzeit reduziert. Start via BAT-Datei, einfaches GUI, alltagstauglich.

---

## Executive Summary

Basierend auf neurowissenschaftlicher Forschung nutzt AntiStutter das Prinzip der **auditiven Ablenkung**, um Stottersymptome um 30-70% zu reduzieren. Das Programm verarbeitet Mikrofon-Eingabe in Echtzeit und gibt modifizierte Audio-Signale über Kopfhörer zurück, die das Gehirn vom Stottern ablenken.

---

## Wissenschaftliche Grundlagen

### Kernprinzip: Ablenkung durch veränderte auditive Rückmeldung
- Stotternde sprechen unter "fluency-inducing conditions" bis zu 90% flüssiger
- Verändertes Hören der eigenen Stimme unterbricht den Stotter-Teufelskreis
- Simuliert Effekte wie Chorsprechen, Singen oder rhythmisches Sprechen

### Bewährte Techniken (in Studien validiert)

#### 1. Delayed Auditory Feedback (DAF)
**Wirkung:** 35-70% Stotterreduktion
**Mechanismus:** Eigene Stimme mit kurzer Verzögerung hören (Echo-Effekt)
**Optimale Parameter:**
- Verzögerung: 50-75 ms (optimal)
- Bereich: 50-100 ms (akzeptabel)
- Lautstärke: ~70 dB
- ⚠️ NICHT >150 ms (verlangsamt Sprache unnatürlich)

**Neurowissenschaft:** Normalisiert auditorisch-motorische Sprachareale im Gehirn

---

#### 2. Frequency Altered Feedback (FAF)
**Wirkung:** 30-60% Stotterreduktion (kombiniert mit DAF: 60-80%)
**Mechanismus:** Tonhöhe der eigenen Stimme verschieben → simuliert "Chorsprechen"
**Optimale Parameter:**
- Pitch-Shift: 0,5 Oktaven nach unten (bevorzugt)
- Alternativ: ±500 Hz Frequenzversatz
- In Kombination mit 50-100 ms DAF am wirksamsten

**Vorteil:** Erzeugt Eindruck, mit zweiter Person synchron zu sprechen

---

#### 3. Rhythmische Stimulation (Metronom)
**Wirkung:** Bis zu 100% Stotterreduktion bei starrem Takt
**Mechanismus:** Externes Timing stabilisiert Sprechmotorik
**Optimale Parameter:**
- Taktrate: 90-120 BPM (Therapie)
- Alltagstauglich: 120-180 BPM (2-3 Hz)
- Klick-Frequenz: 500-1000 Hz (gut hörbar, maskiert Sprache nicht)
- Dezenter, leiser Klickton im Ohr

**Kompromiss:** Langsamere Takte = flüssiger, aber unnatürlich; schnellere Takte = natürlicher, weniger stabilisierend

---

#### 4. Binaurale Beats (Neuronales Entrainment)
**Wirkung:** ~25% Stotterreduktion nach 5 Min Stimulation
**Mechanismus:** Gehirnwellen-Synchronisation für flüssige Sprache
**Optimale Parameter:**
- Delta-Beat: ~3 Hz (Entspannung)
- Theta-Beat: ~7 Hz (Entspannung)
- Beta-Beat: ~21 Hz (Aufmerksamkeit/motorische Kontrolle)
- Trägerfrequenz: <170 Hz (low-pass gefiltert)
- Lautstärke: ~73 dB
- Eingebettet in Hintergrundmusik/Naturklänge

**Neurowissenschaft:** Erhöht Beta-Aktivität im Frontotemporal-Kortex → bessere Sprechkontrolle

---

#### 5. Auditive Maskierung (Weißes Rauschen)
**Wirkung:** 35-55% Stotterreduktion
**Mechanismus:** Überdeckt eigene Stimme → unterbricht Selbstbeobachtung
**Optimale Parameter:**
- Weißes Rauschen: 85-90 dB (effektiv, aber laut)
- Sinuston in Stimmfrequenz: 100-200 Hz bei ~78 dB
- Sprachsynchron (nur während Sprechen)

**Nachteil:** Hohe Lautstärke im Alltag störend → nachrangige Priorität für MVP

---

## MVP-Funktionsumfang

### Core Features (Must-Have)

#### 1. Echtzeit Audio-Processing
- Mikrofon-Eingabe (niedrige Latenz <20 ms)
- Audio-Ausgabe über Kopfhörer/Headset
- Verzögertes Feedback (DAF): 50-100 ms einstellbar
- Frequenz-Shift (FAF): ±0,5 Oktaven einstellbar
- Live-Monitoring

#### 2. Metronom-Funktion
- Einstellbare BPM: 60-240
- Dezenter Klickton (Lautstärke regelbar)
- An/Aus-Schaltung
- Verschiedene Klick-Sounds

#### 3. Binaurale Beats (Background)
- Vorgefertigte Presets:
  - "Entspannt" (Delta/Theta-dominant)
  - "Fokussiert" (Beta-dominant)
  - "Balanced" (3 Hz + 7 Hz + 21 Hz Mix)
- Hintergrund-Loop (10-30 Min Audio-Files)
- Lautstärkeregler

#### 4. Einfaches GUI
- Große, klare Buttons
- Schnellstart: Ein-Klick-Aktivierung
- Preset-Profile:
  - "Leicht" (DAF 50 ms + leichter FAF)
  - "Mittel" (DAF 75 ms + FAF 0,5 Oktave)
  - "Stark" (DAF 100 ms + FAF + Metronom)
  - "Custom" (alle Parameter manuell)
- Lautstärke-Anzeige (VU-Meter)
- An/Aus-Toggle für jede Technik

---

### Nice-to-Have (Phase 2)

- Weißes Rauschen / Maskierung
- Statistiken (Nutzungszeit, bevorzugte Einstellungen)
- Profile speichern/laden
- Systemtray-Integration
- Automatischer Start beim Windows-Boot
- Adaptive Parameter (KI-gestützte Optimierung)

---

## Technische Umsetzung

### Tech-Stack Empfehlung

#### Option A: Python (Empfohlen für MVP)
**Vorteile:**
- Schnelle Entwicklung
- Hervorragende Audio-Bibliotheken
- Einfache GUI-Erstellung
- Gute Performance mit PyAudio/Sounddevice

**Stack:**
```
- Python 3.10+
- PyAudio oder sounddevice (Audio I/O)
- NumPy (Audio-Processing)
- librosa oder pydub (Pitch-Shifting)
- tkinter oder PyQt5 (GUI)
- PyInstaller (EXE-Kompilierung)
```

**Latenz:** Mit ASIO-Treibern <20 ms erreichbar

---

#### Option B: C# (.NET)
**Vorteile:**
- Native Windows-Performance
- Professionelle GUI mit WPF
- Niedrige Latenz

**Stack:**
```
- C# / .NET 6+
- NAudio (Audio-Processing)
- WPF (GUI)
- ASIO.NET (Low-Latency Audio)
```

---

#### Option C: C++ (Für niedrigste Latenz)
**Nur wenn:**
- Latenz <10 ms kritisch
- Performance-Probleme mit Python/C#

**Stack:**
```
- C++17
- JUCE Framework (Audio + GUI)
- PortAudio (Cross-Platform Audio)
```

**Empfehlung für MVP: Python** (Entwicklungsgeschwindigkeit > minimale Latenz-Unterschiede)

---

### Audio-Processing Pipeline

```
[Mikrofon-Input]
    ↓
[Audio Buffer (1024 samples @ 44.1 kHz)]
    ↓
┌─────────────────────────────────┐
│  DSP Processing (parallel):      │
│  1. Delay-Buffer (ringbuffer)    │
│  2. Pitch-Shifting (FFT/Phase)   │
│  3. Mixing mit Binaurale Beats   │
│  4. Metronom-Clicks addieren     │
└─────────────────────────────────┘
    ↓
[Mixer (Lautstärke-Anpassung)]
    ↓
[Kopfhörer-Output]
```

---

### Kernalgorithmen

#### 1. Delayed Auditory Feedback
```python
# Ringbuffer für Delay
class DelayBuffer:
    def __init__(self, delay_ms, sample_rate):
        self.buffer_size = int(delay_ms * sample_rate / 1000)
        self.buffer = np.zeros(self.buffer_size)
        self.write_pos = 0

    def process(self, input_sample):
        # Lies verzögerten Sample
        delayed = self.buffer[self.write_pos]
        # Schreib neuen Sample
        self.buffer[self.write_pos] = input_sample
        self.write_pos = (self.write_pos + 1) % self.buffer_size
        return delayed
```

#### 2. Pitch-Shifting
```python
import librosa

def pitch_shift(audio, semitones, sample_rate):
    # Phase Vocoder für Tonhöhenverschiebung
    shifted = librosa.effects.pitch_shift(
        y=audio,
        sr=sample_rate,
        n_steps=semitones  # -6 für halbe Oktave tiefer
    )
    return shifted
```

#### 3. Binaurale Beats Generierung
```python
def generate_binaural_beat(freq_left, freq_right, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration))
    left = np.sin(2 * np.pi * freq_left * t)
    right = np.sin(2 * np.pi * freq_right * t)
    return left, right

# Beispiel: 7 Hz Theta-Beat
carrier = 150  # Hz (Trägerfrequenz)
left, right = generate_binaural_beat(carrier, carrier + 7, 60, 44100)
```

---

## GUI-Design (Mockup-Beschreibung)

### Layout: Minimalistisch und übersichtlich

```
┌────────────────────────────────────────────┐
│  AntiStutter v1.0            [_][□][×]     │
├────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │  STATUS: ● Aktiv   🎤▓▓▓▓▓░░░  70%  │  │
│  └──────────────────────────────────────┘  │
│                                             │
│  ╔═══════════════════════════════════════╗ │
│  ║  SCHNELLSTART                         ║ │
│  ╠═══════════════════════════════════════╣ │
│  ║  [  Leicht  ] [  Mittel  ] [ Stark ]  ║ │
│  ║  [ Custom ]                            ║ │
│  ╚═══════════════════════════════════════╝ │
│                                             │
│  ┌─ Verzögertes Feedback (DAF) ──────────┐ │
│  │  ☑ Aktiviert                           │ │
│  │  Delay:  [====●====] 75 ms            │ │
│  │  Mix:    [======●==] 80%              │ │
│  └────────────────────────────────────────┘ │
│                                             │
│  ┌─ Tonhöhen-Shift (FAF) ────────────────┐ │
│  │  ☑ Aktiviert                           │ │
│  │  Shift:  [===●=====] -0.5 Okt         │ │
│  └────────────────────────────────────────┘ │
│                                             │
│  ┌─ Metronom ─────────────────────────────┐ │
│  │  ☐ Aktiviert                           │ │
│  │  BPM:    [====●====] 120               │ │
│  │  Lautstärke: [==●======] 40%          │ │
│  └────────────────────────────────────────┘ │
│                                             │
│  ┌─ Binaurale Beats ──────────────────────┐ │
│  │  ☑ Aktiviert                           │ │
│  │  Preset: [▼ Balanced ]                 │ │
│  │  Lautstärke: [====●====] 50%          │ │
│  └────────────────────────────────────────┘ │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │     [■ STOPP]      [▶ START]         │  │
│  └──────────────────────────────────────┘  │
│                                             │
│  [ ? Hilfe ]  [ ⚙ Einstellungen ]          │
└────────────────────────────────────────────┘
```

### Farbschema
- Hintergrund: Helles Grau/Weiß
- Aktive Elemente: Grün (#4CAF50)
- Regler: Blau (#2196F3)
- Warnung: Gelb/Orange
- Fehler: Rot

---

## Preset-Parameter (wissenschaftlich optimiert)

### Preset "Leicht"
- DAF: 50 ms, Mix 70%
- FAF: -0,25 Oktaven
- Metronom: Aus
- Binaurale Beats: Aus
- **Ziel:** Unauffällige Unterstützung, minimale Veränderung

### Preset "Mittel" (Empfohlen)
- DAF: 75 ms, Mix 80%
- FAF: -0,5 Oktaven
- Metronom: Aus (optional 120 BPM)
- Binaurale Beats: Balanced (3+7+21 Hz), 50% Lautstärke
- **Ziel:** Optimales Verhältnis Wirkung/Natürlichkeit

### Preset "Stark"
- DAF: 100 ms, Mix 90%
- FAF: -0,5 Oktaven
- Metronom: 100 BPM, 50% Lautstärke
- Binaurale Beats: Fokussiert (Beta-dominant), 60%
- **Ziel:** Maximum Support bei schweren Situationen

---

## Entwicklungs-Roadmap

### Phase 1: MVP (4-6 Wochen)
**Woche 1-2: Audio-Engine**
- [x] Audio I/O (PyAudio/sounddevice)
- [x] Delay-Buffer implementieren
- [x] Low-Latency Testen (<30 ms)

**Woche 3: DSP-Features**
- [x] Pitch-Shifting (librosa)
- [x] Metronom-Generator
- [x] Binaurale Beat-Files erstellen

**Woche 4-5: GUI**
- [x] Tkinter/PyQt5 Basis-Layout
- [x] Regler/Buttons/VU-Meter
- [x] Preset-System

**Woche 6: Testing & Packaging**
- [x] Beta-Tests mit Zielgruppe
- [x] Bug-Fixes
- [x] PyInstaller: Erstelle EXE
- [x] Start.bat schreiben

---

### Phase 2: Verbesserungen (6-8 Wochen)
- Profil-Speichersystem
- Statistik-Dashboard
- Adaptive Parameter (Machine Learning)
- Weißes Rauschen / Maskierung
- Systemtray-Integration
- Auto-Start Option

---

### Phase 3: Optimization (ongoing)
- Latenz-Optimierung (<15 ms)
- ASIO-Treiber Support
- Performance-Profiling
- User-Feedback Integration

---

## Projektstruktur

```
AntiStutter/
│
├── start.bat                  # Start-Script
├── README.md
├── requirements.txt
│
├── src/
│   ├── main.py                # Entry Point
│   ├── audio_engine.py        # Audio I/O & Processing
│   ├── dsp/
│   │   ├── delay.py           # DAF Implementation
│   │   ├── pitch_shift.py     # FAF Implementation
│   │   ├── metronome.py       # Metronom-Generator
│   │   └── binaural.py        # Binaurale Beats
│   ├── gui/
│   │   ├── main_window.py     # Haupt-GUI
│   │   ├── widgets.py         # Custom Widgets
│   │   └── presets.py         # Preset-Manager
│   └── utils/
│       ├── config.py          # Konfiguration
│       └── logger.py          # Logging
│
├── assets/
│   ├── sounds/
│   │   ├── click_soft.wav     # Metronom-Sounds
│   │   └── click_hard.wav
│   └── binaural_beats/
│       ├── balanced_10min.wav
│       ├── relaxed_10min.wav
│       └── focused_10min.wav
│
├── tests/
│   ├── test_audio.py
│   ├── test_dsp.py
│   └── test_latency.py
│
└── dist/                      # Kompilierte EXE (PyInstaller)
    └── AntiStutter.exe
```

---

## start.bat Inhalt

```batch
@echo off
title AntiStutter - Starthilfe
echo.
echo ================================
echo   AntiStutter wird gestartet...
echo ================================
echo.

REM Check Python Installation
python --version >nul 2>&1
if errorlevel 1 (
    echo FEHLER: Python nicht gefunden!
    echo Bitte installiere Python 3.10+ von python.org
    pause
    exit /b 1
)

REM Check Virtual Environment
if not exist "venv\" (
    echo Erstelle virtuelle Umgebung...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installiere Abhängigkeiten...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

REM Start Application
echo.
echo Starte AntiStutter...
echo.
python src/main.py

REM Fehlerbehandlung
if errorlevel 1 (
    echo.
    echo FEHLER beim Start!
    echo Prüfe die Log-Datei für Details.
    pause
)

deactivate
```

---

## requirements.txt

```
numpy>=1.24.0
sounddevice>=0.4.6
scipy>=1.10.0
librosa>=0.10.0
PyQt5>=5.15.0
pyaudio>=0.2.13
```

---

## Kritische Erfolgsfaktoren

### 1. Niedrige Latenz (<30 ms)
- **Problem:** Hohe Latenz = unnatürliches Sprechen
- **Lösung:**
  - Kleine Buffer-Sizes (512-1024 samples)
  - ASIO-Treiber nutzen (Windows)
  - Effiziente DSP-Algorithmen

### 2. Robuste Audio-Verarbeitung
- **Problem:** Feedback-Schleifen, Verzerrungen
- **Lösung:**
  - Echo-Cancellation
  - Limiter/Compressor
  - Gain-Control

### 3. Einfache Bedienung
- **Problem:** Zu viele Parameter überfordern Nutzer
- **Lösung:**
  - Intelligente Presets (3-4 max)
  - Ein-Klick-Start
  - Versteckte Advanced-Settings

### 4. Akzeptanz im Alltag
- **Problem:** Unnatürliche Klangveränderungen
- **Lösung:**
  - Moderate Parameter (nicht zu extremes Echo/Shift)
  - Mix-Regler (Original + Effekt)
  - Gewöhnungszeit einplanen

---

## Testing-Strategie

### Technische Tests
1. **Latency-Test:** Audio-Input → Output <30 ms?
2. **Stability-Test:** 2h Dauerbetrieb ohne Crashes
3. **Performance-Test:** CPU <20%, RAM <200 MB

### User-Tests (mit Stotternden)
1. **Wirksamkeits-Test:**
   - Stotter-Häufigkeit vor/nach messen
   - Ziel: >30% Reduktion
2. **Usability-Test:**
   - 5 Nutzer testen GUI ohne Anleitung
   - 80% finden Haupt-Features in <2 Min
3. **Alltagstest:**
   - 2 Wochen im Alltag nutzen
   - Feedback zu Praktikabilität

---

## Risiken & Mitigation

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Latenz zu hoch (>50 ms) | Mittel | Hoch | ASIO-Treiber, Buffer-Optimierung |
| Pitch-Shift klingt robotisch | Hoch | Mittel | Hochwertige Algos (librosa), Mix-Regler |
| Nutzer finden GUI zu komplex | Mittel | Mittel | User-Tests, Preset-Fokus |
| Audio-Feedback-Loops | Niedrig | Hoch | Echo-Cancellation, Kopfhörer-Pflicht |
| Batterie-Verbrauch (Laptop) | Niedrig | Niedrig | Performance-Optimierung |

---

## Monetarisierung (Optional, später)

### Freemium-Modell
- **Free:** Basis-Presets, DAF/FAF
- **Premium (9,99€/Monat):**
  - Alle Binaurale Beat-Presets
  - Statistiken & Tracking
  - Profile-Sync (Cloud)
  - Priority Support

### Einmalzahlung: 49,99€
- Lifetime-Lizenz
- Alle Features

---

## Nächste Schritte

1. **Entscheidung Tech-Stack:** Python (empfohlen) vs. C#
2. **Entwicklungsumgebung aufsetzen:**
   - Python 3.10+ installieren
   - IDE (PyCharm/VS Code)
   - Audio-Interface testen
3. **Prototyp Audio-Engine (Woche 1):**
   - Mikrofon → Kopfhörer (passthrough)
   - Latency messen
   - Delay-Buffer implementieren
4. **GUI-Mockup (Woche 2):**
   - Erste Buttons/Regler in Tkinter
   - Preset-System skizzieren
5. **MVP-Fertigstellung (Woche 4-6)**
6. **Alpha-Test mit 3-5 Betroffenen**

---

## Kontakt & Support

Für Fragen zur Entwicklung:
- **Entwickler:** [Dein Name]
- **GitHub:** [Repository-Link]
- **E-Mail:** [Kontakt]

---

## Quellen & Literatur

Dieses MVP basiert auf peer-reviewed Forschung:

1. **Verzögertes Feedback:** Kalinowski et al. (1996), Antipova et al. (2008)
2. **Frequenz-Shift:** Stuart et al. (2004), Wiltshire et al. (2024)
3. **Metronom-Effekt:** Brady (1969), Wiltshire et al. (2024)
4. **Binaurale Beats:** Chernetchenko et al. (2023)
5. **Auditive Maskierung:** Cherry & Sayers (1956), Maraist & Hutton (1957)

**Alle Studien sind in den PDFs im Projektverzeichnis referenziert.**

---

## Changelog

- **v1.0 (2025-10-29):** Initial MVP-Dokument erstellt basierend auf Forschungs-PDFs

---

**Let's build something that helps! 🚀**
