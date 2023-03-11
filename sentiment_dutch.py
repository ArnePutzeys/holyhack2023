from transformers import RobertaTokenizer, RobertaForSequenceClassification
from transformers import pipeline
import torch

#model_name = "DTAI-KULeuven/robbert-v2-dutch-sentiment"
#model = RobertaForSequenceClassification.from_pretrained(model_name)
#tokenizer = RobertaTokenizer.from_pretrained(model_name)

#classifier = pipeline('sentiment-analysis', model=model, tokenizer = tokenizer)

#result1 = classifier('Ik vind het mooi')
# result2 = classifier('Ik vind het lelijk')
# print(result1)
# print(result2)


# Zelfde usage als engelse versie
class Sentiment_dutch:
    def __init__(self):
        self.model_name = "DTAI-KULeuven/robbert-v2-dutch-sentiment"
        self.model = RobertaForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = RobertaTokenizer.from_pretrained(self.model_name)
        self.classifier = pipeline('sentiment-analysis', model=self.model, tokenizer = self.tokenizer)
        self.total_polarity = 0

    def compute_sentiment(self, opinion):
        result = self.classifier(opinion)
        if result[0]['label'] == 'Negative':
            score = 1 - result[0]['score']
        else:
            score = result[0]['score']
        self.total_polarity += score

    def get_sentiment(self, data_length):
        average_polarity = self.total_polarity / data_length
        if self.total_polarity > 0.5:
            overall_sentiment = 'Positive'
        else:
            overall_sentiment = 'Negative'
        return {'average_polarity': average_polarity, 'overall_sentiment': overall_sentiment}