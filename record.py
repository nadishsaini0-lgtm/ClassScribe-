import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

sprate = 16000
duration = 5
frame = int(sprate * duration)
print("speak now")
recording=sd.rec(frame,sprate,1)
sd.wait()
audio_16bit=(recording * 32767).astype(np.int16)
write("test.wav",sprate,audio_16bit)
print("loudest sound ",np.abs(audio_16bit).max())
print("done")