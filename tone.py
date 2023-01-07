import sounddevice as sd
import numpy as np
import sys

frequency = float(sys.argv[1])
duration = float(sys.argv[2])

sampling_rate = 44100

t = np.linspace(0, duration, int(sampling_rate * duration), False)

tone = np.sin(2 * np.pi * frequency * t)

sd.play(tone, blocking=True)
