import whisper

model = whisper.load_model("small")  

def transcribe_audio(path, language=None):
    result = model.transcribe(path, language=language)
    # result contains 'text' plus timestamps if needed
    return result["text"]
