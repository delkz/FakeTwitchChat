from textblob import TextBlob  # Exemplo simples de análise de sentimento

class SentimentAnalysis:
    @staticmethod
    def analyze(text):
        blob = TextBlob(text)
        # Traduz para inglês, se necessário
        if blob.detect_language() != 'en':
            blob = blob.translate(to='en')
        sentiment = blob.sentiment.polarity
        return sentiment
