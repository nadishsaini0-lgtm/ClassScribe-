from stt import transcribe,record_audio,save_notes

#asking for duration
while True:
    try :
        duration = int (input ("For how much duration the recording must go on "))
        break
    except ValueError :
        print("Enter a valid number")
#calling record
record_audio(duration)
#calling transcribe
text=transcribe("audio.wav")
#calling notes_save
save_notes(text)