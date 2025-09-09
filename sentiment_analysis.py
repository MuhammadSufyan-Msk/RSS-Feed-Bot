from transformers import pipeline

# Multilingual sentiment model
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    try:
        result = sentiment_analyzer(text[:512])  # limit length
        return result[0]
    except Exception as e:
        return {"label": "error", "score": 0.0, "error": str(e)}
