"""
Binaural Beats Generator
Based on research: Delta/Theta/Beta beats reduce stuttering by ~25%
Optimal: 3Hz (Delta) + 7Hz (Theta) + 21Hz (Beta) combination
"""

import numpy as np

class BinauralBeatsGenerator:
    """Generate binaural beats for neural entrainment"""

    PRESETS = {
        "relaxed": {
            "beats": [
                {"freq": 3, "carrier": 150, "amplitude": 0.3},   # Delta
                {"freq": 7, "carrier": 160, "amplitude": 0.4},   # Theta
            ]
        },
        "balanced": {
            "beats": [
                {"freq": 3, "carrier": 150, "amplitude": 0.25},  # Delta
                {"freq": 7, "carrier": 160, "amplitude": 0.35},  # Theta
                {"freq": 21, "carrier": 170, "amplitude": 0.4},  # Beta
            ]
        },
        "focused": {
            "beats": [
                {"freq": 7, "carrier": 160, "amplitude": 0.3},   # Theta
                {"freq": 21, "carrier": 170, "amplitude": 0.5},  # Beta
                {"freq": 30, "carrier": 180, "amplitude": 0.2},  # Gamma (light)
            ]
        }
    }

    def __init__(self, sample_rate):
        """
        Initialize binaural beats generator

        Args:
            sample_rate: Audio sample rate
        """
        self.sample_rate = sample_rate
        self.current_preset = "balanced"
        self.phase_left = {}
        self.phase_right = {}

    def generate_stereo(self, num_samples, preset="balanced", volume=0.5):
        """
        Generate stereo binaural beats

        Args:
            num_samples: Number of samples to generate
            preset: Preset name (relaxed, balanced, focused)
            volume: Overall volume (0.0-1.0)

        Returns:
            Tuple of (left_channel, right_channel) as numpy arrays
        """
        if preset not in self.PRESETS:
            preset = "balanced"

        config = self.PRESETS[preset]

        left = np.zeros(num_samples, dtype=np.float32)
        right = np.zeros(num_samples, dtype=np.float32)

        t = np.arange(num_samples) / self.sample_rate

        for beat in config["beats"]:
            freq_diff = beat["freq"]
            carrier = beat["carrier"]
            amplitude = beat["amplitude"]

            # Left ear: carrier frequency
            freq_left = carrier
            # Right ear: carrier + beat frequency
            freq_right = carrier + freq_diff

            # Generate sine waves
            left_wave = amplitude * np.sin(2 * np.pi * freq_left * t)
            right_wave = amplitude * np.sin(2 * np.pi * freq_right * t)

            left += left_wave
            right += right_wave

        # Normalize and apply volume
        max_amp = max(np.max(np.abs(left)), np.max(np.abs(right)))
        if max_amp > 0:
            left = (left / max_amp) * volume
            right = (right / max_amp) * volume

        return left, right

    def generate_mono_mix(self, num_samples, preset="balanced", volume=0.5):
        """
        Generate mono mix of binaural beats
        (Note: True binaural effect requires stereo headphones)

        Returns:
            Mono audio as numpy array
        """
        left, right = self.generate_stereo(num_samples, preset, volume)
        return (left + right) / 2


class BinauralBeatsPlayer:
    """Continuous binaural beats playback with looping"""

    def __init__(self, sample_rate, buffer_size=44100):
        """
        Initialize player

        Args:
            sample_rate: Audio sample rate
            buffer_size: Size of pre-generated buffer (1 second default)
        """
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.generator = BinauralBeatsGenerator(sample_rate)

        # Pre-generate buffers
        self.buffers = {}
        self._generate_buffers()

        # Playback state
        self.position = 0
        self.current_preset = "balanced"

    def _generate_buffers(self):
        """Pre-generate binaural beat buffers for all presets"""
        for preset in BinauralBeatsGenerator.PRESETS.keys():
            left, right = self.generator.generate_stereo(
                self.buffer_size,
                preset=preset,
                volume=1.0  # Volume controlled in playback
            )
            self.buffers[preset] = (left, right)

    def get_samples(self, num_samples, volume=0.5):
        """
        Get next samples from continuous playback

        Args:
            num_samples: Number of samples to retrieve
            volume: Playback volume (0.0-1.0)

        Returns:
            Tuple of (left_channel, right_channel)
        """
        left_buffer, right_buffer = self.buffers[self.current_preset]

        left_out = np.zeros(num_samples, dtype=np.float32)
        right_out = np.zeros(num_samples, dtype=np.float32)

        samples_remaining = num_samples
        out_pos = 0

        while samples_remaining > 0:
            # Calculate how many samples we can take from current position
            available = len(left_buffer) - self.position
            to_take = min(samples_remaining, available)

            # Copy samples
            left_out[out_pos:out_pos + to_take] = left_buffer[self.position:self.position + to_take]
            right_out[out_pos:out_pos + to_take] = right_buffer[self.position:self.position + to_take]

            # Update positions
            self.position += to_take
            out_pos += to_take
            samples_remaining -= to_take

            # Loop if necessary
            if self.position >= len(left_buffer):
                self.position = 0

        # Apply volume
        return left_out * volume, right_out * volume

    def set_preset(self, preset):
        """Change preset"""
        if preset in self.buffers:
            self.current_preset = preset

    def reset(self):
        """Reset playback position"""
        self.position = 0
