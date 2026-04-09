from transcribe import transcribe_audio
from sentiment import analyze_sentiment

path = "samples/sample1.wav"
text = transcribe_audio(path)
label, score = analyze_sentiment(text)

print("Transcript:", text)
print("Sentiment:", label, score)

