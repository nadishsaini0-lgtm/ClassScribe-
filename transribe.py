from faster_whisper import WhisperModel
print("loading...")
model=WhisperModel("small",device="cpu",compute_type="int8")
print("model ready")
segments, info =model.transcribe("test.wav",language="en")
for segment in segments:
    if(segment.end-segment.start>3):
        print(f"[{segment.start:.2f}-{segment.end:.2f}] {segment.text}")