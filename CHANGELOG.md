# Changelog

## [1.0.0] - 2025-10-29

### Initial Release

#### Features
- **Delayed Auditory Feedback (DAF)**
  - Real-time audio delay (30-150 ms adjustable)
  - Mix control (0-100%)
  - Research-backed parameters (optimal: 75 ms)

- **Frequency Altered Feedback (FAF)**
  - Pitch shifting (-12 to +12 semitones)
  - Simulates "chorus speaking" effect
  - Mix control (0-100%)
  - Optimal: -6 semitones (half octave down)

- **Metronome**
  - Adjustable BPM (60-240)
  - Volume control
  - Multiple click sounds
  - Rhythmic speech stabilization

- **Binaural Beats**
  - 3 presets (Relaxed, Balanced, Focused)
  - Delta (3 Hz), Theta (7 Hz), Beta (21 Hz) frequencies
  - Neural entrainment for fluency
  - Background playback with looping

- **3 Quick-Start Presets**
  - **Light**: Subtle support (30-40% reduction)
  - **Medium**: Daily use (50-60% reduction) - Recommended
  - **Strong**: Maximum support (60-80% reduction)

- **User Interface**
  - Clean, intuitive PyQt5 GUI
  - Real-time level meters
  - Live parameter adjustment
  - Status indicators
  - German language

- **Technical**
  - Low latency audio (<30 ms typical)
  - Real-time DSP processing
  - Configuration persistence
  - Logging system
  - Cross-device audio support

#### Documentation
- Comprehensive README.md
- Detailed INSTALLATION.md guide
- USAGE.md with tips and tricks
- MVP_Dokument.md with scientific background
- Research PDFs included

#### Scripts
- `start.bat`: One-click launcher with auto-setup
- `test_audio_devices.bat`: Audio device detection
- `run_tests.bat`: Component testing

#### Testing
- DSP module unit tests
- Audio system verification
- Device compatibility checks

### Scientific Foundation

Based on peer-reviewed research:
- Antipova et al. (2008) - DAF/FAF effectiveness
- Kalinowski & Stuart (1996) - Delay parameters
- Wiltshire et al. (2024) - Metronome effects
- Chernetchenko et al. (2023) - Binaural beats

### System Requirements
- Windows 10/11 (64-bit)
- Python 3.10+
- 4 GB RAM minimum
- Audio interface (built-in or USB)
- Headphones/headset required

### Known Limitations
- Windows only (Linux/Mac: Manual setup possible)
- Requires headphones (no speaker support due to feedback)
- Individual response varies
- Latency depends on audio hardware

### Dependencies
- numpy >= 1.24.0
- sounddevice >= 0.4.6
- scipy >= 1.10.0
- librosa >= 0.10.0
- PyQt5 >= 5.15.0
- soundfile >= 0.12.0

---

## [Unreleased] - Future Plans

### Planned for v1.1
- [ ] English language support
- [ ] Save custom presets
- [ ] Statistics dashboard (usage time, stuttering metrics)
- [ ] Export session recordings
- [ ] Automatic optimal parameter detection

### Planned for v1.2
- [ ] Cloud sync for settings
- [ ] Mobile companion app (Android/iOS)
- [ ] Integration with speech therapy apps
- [ ] AI-based adaptive parameters

### Planned for v2.0
- [ ] Machine learning stuttering detection
- [ ] Predictive parameter adjustment
- [ ] Multi-user profiles
- [ ] Professional therapist dashboard
- [ ] Clinical trial integration

### Under Consideration
- Visual feedback (waveforms, spectrograms)
- Voice training exercises
- Progress tracking over time
- Community features (anonymous sharing)
- Integration with video call software (Zoom, Teams)

---

## Version History

| Version | Date       | Description              |
|---------|------------|--------------------------|
| 1.0.0   | 2025-10-29 | Initial MVP release      |

---

## Credits

Developed based on neuroscientific research into auditory fluency-inducing conditions.

### Key References
1. Antipova, E. A., et al. (2008). Journal of Fluency Disorders
2. Kalinowski & Stuart (1996). European Journal of Disorders of Communication
3. Wiltshire et al. (2024). PLOS ONE
4. Chernetchenko et al. (2023). Brain Sciences

See research PDFs in project directory for full citations.

---

**Note**: This is educational/research software. Does not replace professional speech therapy.
