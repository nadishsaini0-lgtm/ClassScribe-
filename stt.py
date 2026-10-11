import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from faster_whisper import WhisperModel

sprate=16000
print("loading model...")
model=WhisperModel("small",device="cpu",compute_type="int8")
print("model ready")

#Recording audio
def record_audio(duration):
    frame = int(sprate * duration)
    print("speak now")
    recording=sd.rec(frame,sprate,1)
    sd.wait()
    audio_16bit=(recording * 32767).astype(np.int16)
    write("audio.wav",sprate,audio_16bit)
    print("loudest sound ",np.abs(audio_16bit).max())
    print("done")
    


#transcribing audio
def transcribe(audio):
    text = ""
    segments, info = model.transcribe(audio, language="en")
    for segment in segments:
        print(f"[{segment.start:.2f}-{segment.end:.2f}] {segment.text}")
        text+=segment.text
    return text.strip()


#Saving notes
def save_notes(text):
    with open("notes.txt","a", encoding="utf-8") as f:
        f.write(text+"\n") 
    print("notes saved")