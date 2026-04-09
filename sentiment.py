from transformers import pipeline

sentiment_pipe = pipeline("sentiment-analysis")  

def analyze_sentiment(text):
    out = sentiment_pipe(text, truncation=True)[0]
    # example output: {'label': 'POSITIVE', 'score': 0.998}
    return out['label'], out['score']

