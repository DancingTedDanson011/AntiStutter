"""
Main Window for AntiStutter GUI
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QMessageBox, QStatusBar)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon

from audio_engine import AudioEngine
from gui.widgets import LabeledSlider, LevelMeter, ToggleSwitch, ParameterGroup
from gui.presets import PresetSelector, PresetManager
from utils.config import config
from utils.logger import logger


class MainWindow(QMainWindow):
    """Main application window"""

    def __init__(self):
        super().__init__()

        # Audio engine
        self.audio_engine = None

        # UI state
        self.is_running = False

        # Initialize UI
        self.init_ui()

        # Initialize audio engine
        try:
            self.audio_engine = AudioEngine()
        except Exception as e:
            QMessageBox.critical(
                self,
                "Audio Error",
                f"Failed to initialize audio engine:\n{e}\n\n"
                "Please check your audio devices and try again."
            )
            logger.error(f"Failed to initialize audio engine: {e}")

        # Update timer
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_levels)
        self.update_timer.start(50)  # 20 Hz update rate

        logger.info("Main window initialized")

    def init_ui(self):
        """Initialize user interface"""
        self.setWindowTitle("AntiStutter v1.0")
        self.setMinimumSize(600, 800)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        # ===== Status Bar =====
        status_group = ParameterGroup("Status")

        self.status_label = QLabel("● Bereit")
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #666;")

        # Level meters
        level_layout = QHBoxLayout()
        level_layout.addWidget(QLabel("Eingang:"))
        self.input_meter = LevelMeter()
        level_layout.addWidget(self.input_meter, stretch=1)

        status_group.addWidget(self.status_label)
        status_group.addLayout(level_layout)

        main_layout.addWidget(status_group)

        # ===== Preset Selector =====
        preset_group = ParameterGroup("Schnellstart")
        self.preset_selector = PresetSelector()
        self.preset_selector.presetSelected.connect(self.on_preset_selected)
        preset_group.addWidget(self.preset_selector)
        main_layout.addWidget(preset_group)

        # ===== DAF Controls =====
        daf_group = ParameterGroup("Verzögertes Feedback (DAF)")

        self.daf_toggle = ToggleSwitch("Aktiviert", config.get("daf", "enabled"))
        self.daf_toggle.toggled.connect(self.on_daf_toggled)

        self.daf_delay_slider = LabeledSlider(
            "Verzögerung:",
            30, 150,
            config.get("daf", "delay_ms", default=75),
            " ms"
        )
        self.daf_delay_slider.valueChanged.connect(self.on_daf_delay_changed)

        self.daf_mix_slider = LabeledSlider(
            "Mix:",
            0, 100,
            int(config.get("daf", "mix", default=0.8) * 100),
            "%"
        )
        self.daf_mix_slider.valueChanged.connect(self.on_daf_mix_changed)

        daf_group.addWidget(self.daf_toggle)
        daf_group.addWidget(self.daf_delay_slider)
        daf_group.addWidget(self.daf_mix_slider)

        main_layout.addWidget(daf_group)

        # ===== FAF Controls =====
        faf_group = ParameterGroup("Tonhöhen-Shift (FAF)")

        self.faf_toggle = ToggleSwitch("Aktiviert", config.get("faf", "enabled"))
        self.faf_toggle.toggled.connect(self.on_faf_toggled)

        self.faf_shift_slider = LabeledSlider(
            "Tonhöhen-Shift:",
            -12, 12,
            config.get("faf", "semitones", default=-6),
            " Halbtöne"
        )
        self.faf_shift_slider.valueChanged.connect(self.on_faf_shift_changed)

        self.faf_mix_slider = LabeledSlider(
            "Mix:",
            0, 100,
            int(config.get("faf", "mix", default=0.7) * 100),
            "%"
        )
        self.faf_mix_slider.valueChanged.connect(self.on_faf_mix_changed)

        faf_group.addWidget(self.faf_toggle)
        faf_group.addWidget(self.faf_shift_slider)
        faf_group.addWidget(self.faf_mix_slider)

        main_layout.addWidget(faf_group)

        # ===== Metronome Controls =====
        metronome_group = ParameterGroup("Metronom")

        self.metronome_toggle = ToggleSwitch("Aktiviert", config.get("metronome", "enabled"))
        self.metronome_toggle.toggled.connect(self.on_metronome_toggled)

        self.metronome_bpm_slider = LabeledSlider(
            "BPM:",
            60, 240,
            config.get("metronome", "bpm", default=120),
            " BPM"
        )
        self.metronome_bpm_slider.valueChanged.connect(self.on_metronome_bpm_changed)

        self.metronome_volume_slider = LabeledSlider(
            "Lautstärke:",
            0, 100,
            int(config.get("metronome", "volume", default=0.4) * 100),
            "%"
        )
        self.metronome_volume_slider.valueChanged.connect(self.on_metronome_volume_changed)

        metronome_group.addWidget(self.metronome_toggle)
        metronome_group.addWidget(self.metronome_bpm_slider)
        metronome_group.addWidget(self.metronome_volume_slider)

        main_layout.addWidget(metronome_group)

        # ===== Binaural Beats Controls =====
        binaural_group = ParameterGroup("Binaurale Beats")

        self.binaural_toggle = ToggleSwitch("Aktiviert", config.get("binaural", "enabled"))
        self.binaural_toggle.toggled.connect(self.on_binaural_toggled)

        # Preset buttons
        preset_layout = QHBoxLayout()
        self.binaural_presets = {}
        for preset_id, name in [("relaxed", "Entspannt"), ("balanced", "Balanced"), ("focused", "Fokussiert")]:
            btn = QPushButton(name)
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, p=preset_id: self.on_binaural_preset_changed(p))
            self.binaural_presets[preset_id] = btn
            preset_layout.addWidget(btn)

        # Set default
        current_preset = config.get("binaural", "preset", default="balanced")
        if current_preset in self.binaural_presets:
            self.binaural_presets[current_preset].setChecked(True)

        self.binaural_volume_slider = LabeledSlider(
            "Lautstärke:",
            0, 100,
            int(config.get("binaural", "volume", default=0.5) * 100),
            "%"
        )
        self.binaural_volume_slider.valueChanged.connect(self.on_binaural_volume_changed)

        binaural_group.addWidget(self.binaural_toggle)
        binaural_group.addLayout(preset_layout)
        binaural_group.addWidget(self.binaural_volume_slider)

        main_layout.addWidget(binaural_group)

        # ===== Control Buttons =====
        button_layout = QHBoxLayout()

        self.start_button = QPushButton("▶ START")
        self.start_button.setMinimumHeight(50)
        self.start_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.start_button.clicked.connect(self.toggle_processing)

        self.stop_button = QPushButton("■ STOPP")
        self.stop_button.setMinimumHeight(50)
        self.stop_button.setEnabled(False)
        self.stop_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                background-color: #f44336;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
            QPushButton:disabled {
                background-color: #ccc;
            }
        """)
        self.stop_button.clicked.connect(self.toggle_processing)

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)

        main_layout.addLayout(button_layout)

        # ===== Info =====
        info_label = QLabel("💡 Tragen Sie Kopfhörer für optimale Wirkung!")
        info_label.setStyleSheet("color: #666; font-style: italic;")
        info_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(info_label)

        main_layout.addStretch()

        central_widget.setLayout(main_layout)

        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Bereit")

    # ===== Callbacks =====

    def toggle_processing(self):
        """Start/stop audio processing"""
        if not self.audio_engine:
            QMessageBox.warning(self, "Fehler", "Audio-Engine nicht verfügbar!")
            return

        if self.is_running:
            # Stop
            self.audio_engine.stop()
            self.is_running = False
            self.status_label.setText("● Gestoppt")
            self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #f44336;")
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.statusBar.showMessage("Gestoppt")
        else:
            # Start
            try:
                self.audio_engine.start()
                self.is_running = True
                self.status_label.setText("● Aktiv")
                self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #4CAF50;")
                self.start_button.setEnabled(False)
                self.stop_button.setEnabled(True)
                latency = self.audio_engine.get_latency()
                self.statusBar.showMessage(f"Läuft (Latenz: {latency:.1f} ms)")
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Konnte Audio nicht starten:\n{e}")
                logger.error(f"Failed to start audio: {e}")

    def on_preset_selected(self, preset_name):
        """Handle preset selection"""
        logger.info(f"Preset selected: {preset_name}")

        if preset_name != "custom":
            # Apply preset
            PresetManager.apply_preset(preset_name, self.audio_engine)

            # Update UI to reflect preset values
            self.update_ui_from_config()

        # Mark as custom if user changes anything
        config.set("current_preset", value=preset_name)

    def update_ui_from_config(self):
        """Update UI controls from config"""
        # DAF
        self.daf_toggle.setChecked(config.get("daf", "enabled"))
        self.daf_delay_slider.setValue(config.get("daf", "delay_ms"))
        self.daf_mix_slider.setValue(int(config.get("daf", "mix") * 100))

        # FAF
        self.faf_toggle.setChecked(config.get("faf", "enabled"))
        self.faf_shift_slider.setValue(config.get("faf", "semitones"))
        self.faf_mix_slider.setValue(int(config.get("faf", "mix") * 100))

        # Metronome
        self.metronome_toggle.setChecked(config.get("metronome", "enabled"))
        self.metronome_bpm_slider.setValue(config.get("metronome", "bpm"))
        self.metronome_volume_slider.setValue(int(config.get("metronome", "volume") * 100))

        # Binaural
        self.binaural_toggle.setChecked(config.get("binaural", "enabled"))
        self.binaural_volume_slider.setValue(int(config.get("binaural", "volume") * 100))

        preset = config.get("binaural", "preset")
        for pid, btn in self.binaural_presets.items():
            btn.setChecked(pid == preset)

    def on_daf_toggled(self, enabled):
        if self.audio_engine:
            self.audio_engine.toggle_daf(enabled)
        self.preset_selector.setPreset("custom")

    def on_daf_delay_changed(self, value):
        if self.audio_engine:
            self.audio_engine.update_daf_settings(delay_ms=value)
        self.preset_selector.setPreset("custom")

    def on_daf_mix_changed(self, value):
        if self.audio_engine:
            self.audio_engine.update_daf_settings(mix=value / 100.0)
        self.preset_selector.setPreset("custom")

    def on_faf_toggled(self, enabled):
        if self.audio_engine:
            self.audio_engine.toggle_faf(enabled)
        self.preset_selector.setPreset("custom")

    def on_faf_shift_changed(self, value):
        if self.audio_engine:
            self.audio_engine.update_faf_settings(semitones=value)
        self.preset_selector.setPreset("custom")

    def on_faf_mix_changed(self, value):
        if self.audio_engine:
            self.audio_engine.update_faf_settings(mix=value / 100.0)
        self.preset_selector.setPreset("custom")

    def on_metronome_toggled(self, enabled):
        if self.audio_engine:
            self.audio_engine.toggle_metronome(enabled)
        self.preset_selector.setPreset("custom")

    def on_metronome_bpm_changed(self, value):
        if self.audio_engine:
            self.audio_engine.update_metronome_settings(bpm=value)
        self.preset_selector.setPreset("custom")

    def on_metronome_volume_changed(self, value):
        if self.audio_engine:
            self.audio_engine.update_metronome_settings(volume=value / 100.0)
        self.preset_selector.setPreset("custom")

    def on_binaural_toggled(self, enabled):
        if self.audio_engine:
            self.audio_engine.toggle_binaural(enabled)
        self.preset_selector.setPreset("custom")

    def on_binaural_preset_changed(self, preset):
        # Update UI
        for pid, btn in self.binaural_presets.items():
            btn.setChecked(pid == preset)

        if self.audio_engine:
            self.audio_engine.update_binaural_settings(preset=preset)
        self.preset_selector.setPreset("custom")

    def on_binaural_volume_changed(self, value):
        if self.audio_engine:
            self.audio_engine.update_binaural_settings(volume=value / 100.0)
        self.preset_selector.setPreset("custom")

    def update_levels(self):
        """Update level meters"""
        if self.audio_engine and self.is_running:
            input_level = self.audio_engine.get_input_level()
            self.input_meter.setLevel(input_level * 3)  # Scale for visibility

    def closeEvent(self, event):
        """Handle window close"""
        if self.audio_engine and self.is_running:
            self.audio_engine.stop()

        # Save configuration
        config.save()
        logger.info("Application closed")

        event.accept()
