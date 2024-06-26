### This is a script added for your convenience to test your solution. 
### You can run this with the command:
### python -m unittest tests/test_sentiment_analysis.py

import unittest

from sentiment_analysis import sentiment_analysis


class TestAnalyzeSentiment(unittest.TestCase):
    def test_response_type(self):
        """ Test that the sentiment analysis function returns a string. """
        texts = [
            "I love this new song, it's absolutely fantastic!",  # Expected: 'positive'
            "I hate this weather, it's absolutely dreadful!",    # Expected: 'negative'
            "This book is nice, but nothing special about it.",  # Expected: 'neutral'
        ]
        expected_sentiments = ["positive", "negative", "neutral"]
        predicted_sentiments = [
            response.lower() for response in sentiment_analysis(texts)
        ]
        self.assertEqual(predicted_sentiments, expected_sentiments)


if __name__ == '__main__':
    unittest.main()
