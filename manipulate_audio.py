import os
import librosa
import numpy as np
import soundfile as sf

def alter_voice(
    input_path: str,
    output_path: str,
    pitch_steps: float = 0.0,      # Semitones (-12 to +12)
    volume_boost_db: float = 0.0,  # Decibels (-20 to +20)
    speed_rate: float = 1.0,       # Speed multiplier (0.5x to 2.0x)
    reverse: bool = False          # Play backward
) -> str:

    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Load audio signal and preserve original sampling rate
    y, sr = librosa.load(input_path, sr=None)

    # 1. Pitch Shifting (in semitones)
    if pitch_steps != 0.0:
        y = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=pitch_steps)

    # 2. Time Stretching / Speed adjustment
    if speed_rate != 1.0 and speed_rate > 0:
        y = librosa.effects.time_stretch(y=y, rate=speed_rate)

    # 3. Audio Reversal
    if reverse:
        y = np.flip(y)

    # 4. Volume Scaling (Decibel gain adjustment)
    if volume_boost_db != 0.0:
        multiplier = 10 ** (volume_boost_db / 20.0)
        y = y * multiplier
        # Clip peak values to prevent digital clipping/distortion
        y = np.clip(y, -1.0, 1.0)

    # Create destination directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(output_path))
    os.makedirs(output_dir, exist_ok=True)

    # Write processed audio array to file
    sf.write(output_path, y, sr)

    return os.path.abspath(output_path)