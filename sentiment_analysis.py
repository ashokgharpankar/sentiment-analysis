
---

### 3. `sentiment_analysis.py`

```python
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # Load a pretrained sentiment-analysis pipeline
        self.analyzer = pipeline("sentiment-analysis")

    def analyze(self, text: str):
        # Returns sentiment label and score
        result = self.analyzer(text)[0]
        return {
            "label": result["label"],
            "score": result["score"]
        }

if __name__ == "__main__":
    sa = SentimentAnalyzer()
    test_text = "I love using stomp.sg for the latest news!"
    sentiment = sa.analyze(test_text)
    print(f"Text: {test_text}\nSentiment: {sentiment}")
