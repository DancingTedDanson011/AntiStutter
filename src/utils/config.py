"""
Configuration Management for AntiStutter
"""

import json
import os
from pathlib import Path

class Config:
    """Application configuration manager"""

    # Default configuration
    DEFAULTS = {
        "audio": {
            "sample_rate": 44100,
            "buffer_size": 1024,
            "channels": 1,
            "input_device": None,  # None = default device
            "output_device": None
        },
        "daf": {  # Delayed Auditory Feedback
            "enabled": True,
            "delay_ms": 75,
            "mix": 0.8  # 0.0-1.0
        },
        "faf": {  # Frequency Altered Feedback
            "enabled": True,
            "semitones": -6,  # -6 = half octave down
            "mix": 0.7
        },
        "metronome": {
            "enabled": False,
            "bpm": 120,
            "volume": 0.4
        },
        "binaural": {
            "enabled": True,
            "preset": "balanced",  # balanced, relaxed, focused
            "volume": 0.5
        },
        "presets": {
            "light": {
                "daf": {"enabled": True, "delay_ms": 50, "mix": 0.7},
                "faf": {"enabled": True, "semitones": -3, "mix": 0.6},
                "metronome": {"enabled": False},
                "binaural": {"enabled": False}
            },
            "medium": {
                "daf": {"enabled": True, "delay_ms": 75, "mix": 0.8},
                "faf": {"enabled": True, "semitones": -6, "mix": 0.7},
                "metronome": {"enabled": False},
                "binaural": {"enabled": True, "preset": "balanced", "volume": 0.5}
            },
            "strong": {
                "daf": {"enabled": True, "delay_ms": 100, "mix": 0.9},
                "faf": {"enabled": True, "semitones": -6, "mix": 0.8},
                "metronome": {"enabled": True, "bpm": 100, "volume": 0.5},
                "binaural": {"enabled": True, "preset": "focused", "volume": 0.6}
            }
        }
    }

    def __init__(self):
        self.config_dir = Path.home() / ".antistutter"
        self.config_file = self.config_dir / "config.json"
        self.settings = self.DEFAULTS.copy()
        self.load()

    def load(self):
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self._merge_config(self.settings, loaded)
            except Exception as e:
                print(f"Error loading config: {e}")

    def save(self):
        """Save configuration to file"""
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")

    def _merge_config(self, base, update):
        """Recursively merge configuration dictionaries"""
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value

    def get(self, *keys, default=None):
        """Get nested configuration value"""
        value = self.settings
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value

    def set(self, *keys, value):
        """Set nested configuration value"""
        target = self.settings
        for key in keys[:-1]:
            if key not in target:
                target[key] = {}
            target = target[key]
        target[keys[-1]] = value

    def apply_preset(self, preset_name):
        """Apply a preset configuration"""
        preset = self.get("presets", preset_name)
        if preset:
            for module, settings in preset.items():
                for key, value in settings.items():
                    self.set(module, key, value=value)
            return True
        return False

# Global config instance
config = Config()
