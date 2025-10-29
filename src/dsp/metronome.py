"""
Metronome Implementation
Based on research: Rhythmic stimulation reduces stuttering up to 100%
Optimal: 90-180 BPM for natural speech
"""

import numpy as np

class Metronome:
    """Simple metronome with adjustable BPM and volume"""

    def __init__(self, sample_rate, bpm=120, volume=0.5):
        """
        Initialize metronome

        Args:
            sample_rate: Audio sample rate
            bpm: Beats per minute (60-240 typical)
            volume: Click volume (0.0-1.0)
        """
        self.sample_rate = sample_rate
        self.bpm = bpm
        self.volume = volume

        # Calculate samples between clicks
        self.update_timing()

        # Click sound generation
        self.click_duration = 0.01  # 10ms click
        self.click_samples = int(self.click_duration * sample_rate)
        self.click_sound = self._generate_click()

        # State
        self.sample_counter = 0
        self.click_position = 0
        self.playing_click = False

    def update_timing(self):
        """Update timing based on BPM"""
        seconds_per_beat = 60.0 / self.bpm
        self.samples_per_beat = int(seconds_per_beat * self.sample_rate)

    def _generate_click(self):
        """Generate click sound (simple sine wave envelope)"""
        t = np.linspace(0, self.click_duration, self.click_samples)

        # 1000 Hz sine wave with exponential decay
        frequency = 1000
        click = np.sin(2 * np.pi * frequency * t)
        envelope = np.exp(-t * 100)  # Decay

        return click * envelope

    def process(self, num_samples):
        """
        Generate metronome clicks

        Args:
            num_samples: Number of samples to generate

        Returns:
            Audio samples with metronome clicks
        """
        output = np.zeros(num_samples, dtype=np.float32)

        for i in range(num_samples):
            # Check if we should start a new click
            if self.sample_counter >= self.samples_per_beat:
                self.sample_counter = 0
                self.playing_click = True
                self.click_position = 0

            # Add click sound if playing
            if self.playing_click:
                if self.click_position < len(self.click_sound):
                    output[i] = self.click_sound[self.click_position] * self.volume
                    self.click_position += 1
                else:
                    self.playing_click = False

            self.sample_counter += 1

        return output

    def set_bpm(self, bpm):
        """Change BPM"""
        self.bpm = max(30, min(300, bpm))  # Limit to reasonable range
        self.update_timing()

    def set_volume(self, volume):
        """Change volume (0.0-1.0)"""
        self.volume = max(0.0, min(1.0, volume))

    def reset(self):
        """Reset metronome to start of beat"""
        self.sample_counter = 0
        self.click_position = 0
        self.playing_click = False
