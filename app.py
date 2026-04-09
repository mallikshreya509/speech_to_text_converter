import streamlit as st
from transcribe import transcribe_audio
from sentiment import analyze_sentiment
from audio_emotion import audio_emotion  

st.title("Speech → Transcript + Sentiment")

uploaded = st.file_uploader("Upload WAV/MP3", type=["wav","mp3","m4a"])
if uploaded:
    with open("temp_audio.wav","wb") as f:
        f.write(uploaded.read())
    st.info("Transcribing...")
    transcript = transcribe_audio("temp_audio.wav")
    st.subheader("Transcript")
    st.write(transcript)

    st.info("Analyzing sentiment..")
    label, score = analyze_sentiment(transcript)
    st.subheader("Text Sentiment")
    st.write(f"{label} ({score:.2f})")

    # optional
    try:
        emo = audio_emotion("temp_audio.wav")
        st.subheader("Audio Emotions (top 3)")
        for l,s in emo[:3]:
            st.write(f"{l}: {s:.2f}")
    except Exception as e:
        st.write("Audio emotion model not available or failed:", e)
