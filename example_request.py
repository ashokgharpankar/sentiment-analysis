from sentiment_analysis import SentimentAnalyzer

def main():
    sa = SentimentAnalyzer()
    
    samples = [
        "I love the new article format on stomp.sg!",
        "This news story is disappointing and sad.",
        "I have no strong feelings about this article."
    ]

    for text in samples:
        result = sa.analyze(text)
        print(f"Text: {text}\nSentiment: {result}\n")

if __name__ == "__main__":
    main()
