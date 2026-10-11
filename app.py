import streamlit as st
from stt import record_audio,transcribe,save_notes

st.title("Speech To Text Convertion")
number=st.slider("pick the duration of recording",1, 59)
button=st.button("Record")
if button:
    st.write(f"The recording will go upto {number} seconds")
    with st.spinner("Start recording"):
        record_audio(number)
    
    with st.spinner("Transcribing is going on"):
        text = transcribe("audio.wav")
    st.write(text)

    save_notes(text)

try:
    with open("notes.txt", "r", encoding="utf-8") as f:
        st.write(f.read())
except FileNotFoundError:
    st.text("No notes yet")