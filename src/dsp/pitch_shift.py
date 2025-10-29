"""
Frequency Altered Feedback (FAF) Implementation
Based on research: -0.5 octave shift reduces stuttering by 30-60%
Simulates "chorus speaking" effect
"""

import numpy as np
from scipy import signal

class PitchShifter:
    """Real-time pitch shifter using phase vocoder"""

    def __init__(self, sample_rate, frame_size=2048):
        """
        Initialize pitch shifter

        Args:
            sample_rate: Audio sample rate
            frame_size: FFT frame size (larger = better quality, more latency)
        """
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.hop_size = frame_size // 4

        # Buffers
        self.input_buffer = np.zeros(frame_size)
        self.output_buffer = np.zeros(frame_size)
        self.phase = np.zeros(frame_size // 2 + 1)
        self.last_phase = np.zeros(frame_size // 2 + 1)

        # Window function
        self.window = np.hanning(frame_size)

    def shift_semitones(self, audio, semitones):
        """
        Shift pitch by semitones

        Args:
            audio: Input audio samples
            semitones: Number of semitones to shift (-6 = half octave down)

        Returns:
            Pitch-shifted audio
        """
        if semitones == 0:
            return audio

        # Simple implementation using resampling
        # For better quality, use librosa in production
        ratio = 2 ** (semitones / 12.0)

        # Resample
        num_samples = int(len(audio) / ratio)
        indices = np.arange(num_samples) * ratio

        # Interpolate
        shifted = np.interp(indices, np.arange(len(audio)), audio)

        # Adjust length to match input
        if len(shifted) < len(audio):
            # Pad with zeros
            shifted = np.pad(shifted, (0, len(audio) - len(shifted)), mode='constant')
        elif len(shifted) > len(audio):
            # Truncate
            shifted = shifted[:len(audio)]

        return shifted

    def process(self, audio, semitones):
        """
        Process audio with pitch shifting

        Args:
            audio: Input audio samples
            semitones: Number of semitones to shift

        Returns:
            Pitch-shifted audio
        """
        return self.shift_semitones(audio, semitones)


class SimplePitchShifter:
    """
    Simplified pitch shifter using librosa when available
    Falls back to basic method if librosa not available
    """

    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.use_librosa = False

        try:
            import librosa
            self.librosa = librosa
            self.use_librosa = True
        except ImportError:
            pass

    def process(self, audio, semitones):
        """Process audio with pitch shifting"""
        if self.use_librosa and semitones != 0:
            try:
                return self.librosa.effects.pitch_shift(
                    y=audio,
                    sr=self.sample_rate,
                    n_steps=semitones
                )
            except Exception:
                # Fallback
                pass

        # Fallback: use basic pitch shifter
        shifter = PitchShifter(self.sample_rate)
        return shifter.process(audio, semitones)
