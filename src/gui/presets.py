"""
Preset Manager for AntiStutter
"""

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import pyqtSignal

from utils.config import config


class PresetSelector(QWidget):
    """Preset selection buttons"""

    presetSelected = pyqtSignal(str)

    PRESETS = {
        "light": {
            "name": "Leicht",
            "description": "Unauffällige Unterstützung"
        },
        "medium": {
            "name": "Mittel",
            "description": "Empfohlen für Alltag"
        },
        "strong": {
            "name": "Stark",
            "description": "Maximale Unterstützung"
        },
        "custom": {
            "name": "Custom",
            "description": "Eigene Einstellungen"
        }
    }

    def __init__(self, parent=None):
        super().__init__(parent)

        self.current_preset = "medium"
        self.buttons = {}

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        for preset_id, preset_info in self.PRESETS.items():
            btn = QPushButton(preset_info["name"])
            btn.setToolTip(preset_info["description"])
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, p=preset_id: self._on_preset_clicked(p))

            # Styling
            btn.setMinimumHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 14px;
                    font-weight: bold;
                    background-color: #f0f0f0;
                    border: 2px solid #ccc;
                    border-radius: 5px;
                    padding: 5px 15px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
                QPushButton:checked {
                    background-color: #4CAF50;
                    color: white;
                    border-color: #4CAF50;
                }
            """)

            self.buttons[preset_id] = btn
            layout.addWidget(btn)

        self.setLayout(layout)

        # Set default
        self.buttons["medium"].setChecked(True)

    def _on_preset_clicked(self, preset_id):
        """Handle preset button click"""
        # Uncheck all other buttons
        for pid, btn in self.buttons.items():
            btn.setChecked(pid == preset_id)

        self.current_preset = preset_id
        self.presetSelected.emit(preset_id)

    def setPreset(self, preset_id):
        """Set current preset"""
        if preset_id in self.buttons:
            self._on_preset_clicked(preset_id)

    def getCurrentPreset(self):
        """Get current preset ID"""
        return self.current_preset


class PresetManager:
    """Manage preset loading and application"""

    @staticmethod
    def apply_preset(preset_name, audio_engine):
        """
        Apply preset to audio engine

        Args:
            preset_name: Name of preset (light, medium, strong)
            audio_engine: AudioEngine instance
        """
        if preset_name == "custom":
            return  # Don't change settings for custom

        # Apply preset from config
        success = config.apply_preset(preset_name)

        if success and audio_engine:
            # Update DAF
            audio_engine.update_daf_settings(
                delay_ms=config.get("daf", "delay_ms"),
                mix=config.get("daf", "mix")
            )
            audio_engine.toggle_daf(config.get("daf", "enabled"))

            # Update FAF
            audio_engine.update_faf_settings(
                semitones=config.get("faf", "semitones"),
                mix=config.get("faf", "mix")
            )
            audio_engine.toggle_faf(config.get("faf", "enabled"))

            # Update Metronome
            audio_engine.update_metronome_settings(
                bpm=config.get("metronome", "bpm"),
                volume=config.get("metronome", "volume")
            )
            audio_engine.toggle_metronome(config.get("metronome", "enabled"))

            # Update Binaural
            audio_engine.update_binaural_settings(
                preset=config.get("binaural", "preset"),
                volume=config.get("binaural", "volume")
            )
            audio_engine.toggle_binaural(config.get("binaural", "enabled"))

        return success

    @staticmethod
    def get_preset_settings(preset_name):
        """Get settings for a preset"""
        return config.get("presets", preset_name)
