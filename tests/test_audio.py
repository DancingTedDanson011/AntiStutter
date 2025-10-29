"""
Basic audio system tests
"""

import numpy as np
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from dsp.delay import DelayBuffer
from dsp.pitch_shift import SimplePitchShifter
from dsp.metronome import Metronome
from dsp.binaural import BinauralBeatsGenerator


def test_delay_buffer():
    """Test delay buffer"""
    print("Testing DelayBuffer...")

    sample_rate = 44100
    delay_ms = 75
    buffer = DelayBuffer(delay_ms, sample_rate)

    # Generate test signal
    duration = 0.1  # 100ms
    num_samples = int(duration * sample_rate)
    test_signal = np.random.randn(num_samples).astype(np.float32)

    # Process
    output = buffer.process(test_signal)

    assert output.shape == test_signal.shape
    print("✓ DelayBuffer works!")


def test_pitch_shifter():
    """Test pitch shifter"""
    print("Testing PitchShifter...")

    sample_rate = 44100
    shifter = SimplePitchShifter(sample_rate)

    # Generate test signal (sine wave)
    duration = 0.1
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples)
    test_signal = np.sin(2 * np.pi * 440 * t).astype(np.float32)  # 440 Hz

    # Shift down by half octave
    output = shifter.process(test_signal, -6)

    assert output.shape == test_signal.shape
    print("✓ PitchShifter works!")


def test_metronome():
    """Test metronome"""
    print("Testing Metronome...")

    sample_rate = 44100
    metronome = Metronome(sample_rate, bpm=120, volume=0.5)

    # Generate 1 second
    num_samples = sample_rate
    output = metronome.process(num_samples)

    assert output.shape == (num_samples,)
    assert np.max(np.abs(output)) > 0  # Should have clicks
    print("✓ Metronome works!")


def test_binaural_beats():
    """Test binaural beats"""
    print("Testing BinauralBeats...")

    sample_rate = 44100
    generator = BinauralBeatsGenerator(sample_rate)

    # Generate 1 second stereo
    num_samples = sample_rate
    left, right = generator.generate_stereo(num_samples, preset="balanced", volume=0.5)

    assert left.shape == (num_samples,)
    assert right.shape == (num_samples,)
    assert not np.array_equal(left, right)  # Should be different (binaural)
    print("✓ BinauralBeats works!")


def main():
    """Run all tests"""
    print("=" * 50)
    print("Running Audio System Tests")
    print("=" * 50)
    print()

    try:
        test_delay_buffer()
        test_pitch_shifter()
        test_metronome()
        test_binaural_beats()

        print()
        print("=" * 50)
        print("✓ All tests passed!")
        print("=" * 50)

    except Exception as e:
        print()
        print("=" * 50)
        print(f"✗ Test failed: {e}")
        print("=" * 50)
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
