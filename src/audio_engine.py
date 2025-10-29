"""
Audio Engine for AntiStutter
Real-time audio processing with low latency
"""

import numpy as np
import sounddevice as sd
import threading
import time
from queue import Queue

from dsp.delay import DelayBuffer
from dsp.pitch_shift import SimplePitchShifter
from dsp.metronome import Metronome
from dsp.binaural import BinauralBeatsPlayer
from utils.logger import logger
from utils.config import config


class AudioEngine:
    """Real-time audio processing engine"""

    def __init__(self):
        """Initialize audio engine"""
        # Audio parameters
        self.sample_rate = config.get("audio", "sample_rate", default=44100)
        self.buffer_size = config.get("audio", "buffer_size", default=1024)
        self.channels = config.get("audio", "channels", default=1)

        # DSP modules
        self.delay_buffer = None
        self.pitch_shifter = None
        self.metronome = None
        self.binaural_player = None

        # State
        self.is_running = False
        self.stream = None
        self.input_level = 0.0
        self.output_level = 0.0

        # Statistics
        self.latency_ms = 0.0
        self.cpu_load = 0.0

        # Initialize DSP modules
        self._initialize_dsp()

        logger.info("Audio Engine initialized")
        logger.info(f"Sample Rate: {self.sample_rate} Hz")
        logger.info(f"Buffer Size: {self.buffer_size} samples")
        logger.info(f"Latency: ~{(self.buffer_size / self.sample_rate) * 1000:.1f} ms")

    def _initialize_dsp(self):
        """Initialize all DSP modules"""
        # Delay buffer
        delay_ms = config.get("daf", "delay_ms", default=75)
        self.delay_buffer = DelayBuffer(delay_ms, self.sample_rate)

        # Pitch shifter
        self.pitch_shifter = SimplePitchShifter(self.sample_rate)

        # Metronome
        bpm = config.get("metronome", "bpm", default=120)
        volume = config.get("metronome", "volume", default=0.4)
        self.metronome = Metronome(self.sample_rate, bpm, volume)

        # Binaural beats player
        self.binaural_player = BinauralBeatsPlayer(self.sample_rate, self.sample_rate)
        preset = config.get("binaural", "preset", default="balanced")
        self.binaural_player.set_preset(preset)

    def _audio_callback(self, indata, outdata, frames, time_info, status):
        """
        Audio callback function (called by sounddevice)

        Args:
            indata: Input audio data
            outdata: Output audio buffer
            frames: Number of frames
            time_info: Timing information
            status: Status flags
        """
        if status:
            logger.warning(f"Audio callback status: {status}")

        try:
            # Get input audio (mono)
            if self.channels == 1:
                input_audio = indata[:, 0].copy()
            else:
                input_audio = np.mean(indata, axis=1)

            # Calculate input level
            self.input_level = np.sqrt(np.mean(input_audio ** 2))

            # Start with input audio
            output_audio = input_audio.copy()
            dry_signal = input_audio.copy()

            # Apply DAF (Delayed Auditory Feedback)
            if config.get("daf", "enabled", default=True):
                delayed = self.delay_buffer.process(input_audio)
                mix = config.get("daf", "mix", default=0.8)
                output_audio = dry_signal * (1 - mix) + delayed * mix

            # Apply FAF (Frequency Altered Feedback)
            if config.get("faf", "enabled", default=True):
                semitones = config.get("faf", "semitones", default=-6)
                mix = config.get("faf", "mix", default=0.7)

                # Pitch shift the current output
                shifted = self.pitch_shifter.process(output_audio, semitones)

                # Mix with unshifted
                output_audio = output_audio * (1 - mix) + shifted * mix

            # Add Metronome
            if config.get("metronome", "enabled", default=False):
                metronome_audio = self.metronome.process(frames)
                output_audio = output_audio + metronome_audio

            # Add Binaural Beats (stereo)
            stereo_output = np.zeros((frames, 2), dtype=np.float32)

            if config.get("binaural", "enabled", default=True):
                volume = config.get("binaural", "volume", default=0.5)
                left, right = self.binaural_player.get_samples(frames, volume)

                # Mix with output audio
                stereo_output[:, 0] = output_audio + left
                stereo_output[:, 1] = output_audio + right
            else:
                # Mono to stereo
                stereo_output[:, 0] = output_audio
                stereo_output[:, 1] = output_audio

            # Normalize to prevent clipping
            max_val = np.max(np.abs(stereo_output))
            if max_val > 0.95:
                stereo_output = stereo_output * (0.95 / max_val)

            # Calculate output level
            self.output_level = np.sqrt(np.mean(stereo_output ** 2))

            # Write to output
            outdata[:] = stereo_output

        except Exception as e:
            logger.error(f"Error in audio callback: {e}")
            outdata.fill(0)

    def start(self):
        """Start audio processing"""
        if self.is_running:
            logger.warning("Audio engine already running")
            return

        try:
            # Get device info
            input_device = config.get("audio", "input_device")
            output_device = config.get("audio", "output_device")

            logger.info("Starting audio stream...")
            logger.info(f"Input device: {input_device or 'Default'}")
            logger.info(f"Output device: {output_device or 'Default'}")

            # Create and start stream
            self.stream = sd.Stream(
                samplerate=self.sample_rate,
                blocksize=self.buffer_size,
                device=(input_device, output_device),
                channels=(1, 2),  # Mono input, stereo output
                callback=self._audio_callback,
                dtype=np.float32
            )

            self.stream.start()
            self.is_running = True

            # Get actual latency
            self.latency_ms = self.stream.latency[1] * 1000

            logger.info("Audio stream started successfully")
            logger.info(f"Actual latency: {self.latency_ms:.1f} ms")

        except Exception as e:
            logger.error(f"Failed to start audio stream: {e}")
            raise

    def stop(self):
        """Stop audio processing"""
        if not self.is_running:
            return

        logger.info("Stopping audio stream...")

        try:
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.stream = None

            self.is_running = False
            logger.info("Audio stream stopped")

        except Exception as e:
            logger.error(f"Error stopping audio stream: {e}")

    def update_daf_settings(self, delay_ms=None, mix=None):
        """Update DAF settings"""
        if delay_ms is not None:
            self.delay_buffer.set_delay(delay_ms)
            config.set("daf", "delay_ms", value=delay_ms)
            logger.debug(f"DAF delay updated: {delay_ms} ms")

        if mix is not None:
            config.set("daf", "mix", value=mix)
            logger.debug(f"DAF mix updated: {mix}")

    def update_faf_settings(self, semitones=None, mix=None):
        """Update FAF settings"""
        if semitones is not None:
            config.set("faf", "semitones", value=semitones)
            logger.debug(f"FAF semitones updated: {semitones}")

        if mix is not None:
            config.set("faf", "mix", value=mix)
            logger.debug(f"FAF mix updated: {mix}")

    def update_metronome_settings(self, bpm=None, volume=None):
        """Update metronome settings"""
        if bpm is not None:
            self.metronome.set_bpm(bpm)
            config.set("metronome", "bpm", value=bpm)
            logger.debug(f"Metronome BPM updated: {bpm}")

        if volume is not None:
            self.metronome.set_volume(volume)
            config.set("metronome", "volume", value=volume)
            logger.debug(f"Metronome volume updated: {volume}")

    def update_binaural_settings(self, preset=None, volume=None):
        """Update binaural beats settings"""
        if preset is not None:
            self.binaural_player.set_preset(preset)
            config.set("binaural", "preset", value=preset)
            logger.debug(f"Binaural preset updated: {preset}")

        if volume is not None:
            config.set("binaural", "volume", value=volume)
            logger.debug(f"Binaural volume updated: {volume}")

    def toggle_daf(self, enabled):
        """Enable/disable DAF"""
        config.set("daf", "enabled", value=enabled)
        logger.info(f"DAF {'enabled' if enabled else 'disabled'}")

    def toggle_faf(self, enabled):
        """Enable/disable FAF"""
        config.set("faf", "enabled", value=enabled)
        logger.info(f"FAF {'enabled' if enabled else 'disabled'}")

    def toggle_metronome(self, enabled):
        """Enable/disable metronome"""
        config.set("metronome", "enabled", value=enabled)
        if enabled:
            self.metronome.reset()
        logger.info(f"Metronome {'enabled' if enabled else 'disabled'}")

    def toggle_binaural(self, enabled):
        """Enable/disable binaural beats"""
        config.set("binaural", "enabled", value=enabled)
        if enabled:
            self.binaural_player.reset()
        logger.info(f"Binaural beats {'enabled' if enabled else 'disabled'}")

    def get_input_level(self):
        """Get current input level (0.0-1.0)"""
        return self.input_level

    def get_output_level(self):
        """Get current output level (0.0-1.0)"""
        return self.output_level

    def get_latency(self):
        """Get current latency in milliseconds"""
        return self.latency_ms

    @staticmethod
    def list_devices():
        """List available audio devices"""
        devices = sd.query_devices()
        logger.info("Available audio devices:")
        for i, device in enumerate(devices):
            logger.info(f"  {i}: {device['name']}")
            logger.info(f"      Inputs: {device['max_input_channels']}, "
                       f"Outputs: {device['max_output_channels']}")
        return devices
