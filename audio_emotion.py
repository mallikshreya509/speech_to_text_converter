from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
import torch
import soundfile as sf
import librosa

MODEL_NAME = "superb/hubert-base-superb-er"

feat = AutoFeatureExtractor.from_pretrained(MODEL_NAME)
model = AutoModelForAudioClassification.from_pretrained(MODEL_NAME)

def audio_emotion(path):
    # Load audio file
    signal, sr = sf.read(path)

    # Convert stereo → mono if needed
    if len(signal.shape) > 1:
        signal = signal.mean(axis=1)

    # ✅ Resample audio to 16 kHz (model requirement)
    if sr != 16000:
        signal = librosa.resample(signal, orig_sr=sr, target_sr=16000)
        sr = 16000

    # Prepare input
    inputs = feat(signal, sampling_rate=sr, return_tensors="pt", padding=True)

    # Inference
    with torch.no_grad():
        logits = model(**inputs).logits
        scores = torch.softmax(logits, dim=1).squeeze().tolist()
        labels = model.config.id2label

    # Rank top emotions
    ranked = sorted(zip(labels.values(), scores), key=lambda x: x[1], reverse=True)
    return ranked
