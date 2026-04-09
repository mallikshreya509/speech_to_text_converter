## 🧠 About:

The Speech-to-Text and Emotion Analyzer is an intelligent AI application that converts spoken audio into text and then analyzes the sentiment or emotional tone of the speech.
It uses OpenAI Whisper for transcription and Hugging Face emotion models for emotion detection.
This combination enables users to gain deeper insights into both what was said and how it was said — a key advantage for communication analysis, customer service, mental health support, and other applications.


## ⚙️ Tech Stack:

 Python 3.11

 OpenAI Whisper – speech-to-text model

 Transformers (Hugging Face) – emotion/sentiment analysis

 Librosa, SoundFile, Pydub – audio preprocessing

 Streamlit – interactive web UI


## 🧩 1. Prerequisites

Make sure you have:

->Python 3.9+

->pip (Python package manager)

->ffmpeg installed (needed by Whisper + pydub)


## 🧱 2. Create and set up your project folder

Open your terminal, and run:

mkdir speech-sentiment

cd speech-sentiment

python3 -m venv venv

source venv/bin/activate # On macOS/Linux

venv\Scripts\activate on Windows

pip install --upgrade pip

pip install openai-whisper transformers torch librosa soundfile pydub streamlit

## 3. 🚀 9. Run the Streamlit app

From your project folder:

streamlit run app.py

This will open a browser window at:
```bash
http://localhost:8501
```

You’ll see a simple UI where you can upload your sample audio (e.g., samples/sample1.wav)
→ The app will transcribe it
→ Then analyze the sentiment
→ And display both results.


## 🧰 Setup Instructions

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/butterflysly53/speech-to-text-converter.git
cd speech-to-text-converter
