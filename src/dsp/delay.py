"""
Delayed Auditory Feedback (DAF) Implementation
Based on research: 50-100ms delay reduces stuttering by 30-70%
"""

import numpy as np

class DelayBuffer:
    """Ring buffer for audio delay"""

    def __init__(self, delay_ms, sample_rate):
        """
        Initialize delay buffer

        Args:
            delay_ms: Delay time in milliseconds (50-100 recommended)
            sample_rate: Audio sample rate (e.g., 44100)
        """
        self.delay_ms = delay_ms
        self.sample_rate = sample_rate
        self.buffer_size = int((delay_ms / 1000.0) * sample_rate)
        self.buffer = np.zeros(self.buffer_size, dtype=np.float32)
        self.write_pos = 0

    def process(self, input_audio):
        """
        Process audio through delay buffer

        Args:
            input_audio: Input audio samples (numpy array)

        Returns:
            Delayed audio samples
        """
        output = np.zeros_like(input_audio)

        for i in range(len(input_audio)):
            # Read delayed sample
            output[i] = self.buffer[self.write_pos]

            # Write new sample
            self.buffer[self.write_pos] = input_audio[i]

            # Advance write position (ring buffer)
            self.write_pos = (self.write_pos + 1) % self.buffer_size

        return output

    def set_delay(self, delay_ms):
        """Change delay time (clears buffer)"""
        if delay_ms != self.delay_ms:
            self.delay_ms = delay_ms
            self.buffer_size = int((delay_ms / 1000.0) * self.sample_rate)
            self.buffer = np.zeros(self.buffer_size, dtype=np.float32)
            self.write_pos = 0

    def clear(self):
        """Clear the delay buffer"""
        self.buffer.fill(0)
        self.write_pos = 0
