import json
from textblob import TextBlob

# Usage: 1) Call sentiment = Sentiment()
#        2) Call sentiment.compute_sentiment(opinion) inside the loop
#        3) Call sentiment.get_sentiment(data_length) after the loop. This returns a dictionary of the following format:
#           {'average_polarity': average_polarity, 'average_subjectivity': average_subjectivity, 'overall_sentiment': overall_sentiment}
#        
class Sentiment:
    def __init__(self):
        self.total_polarity = 0
        self.total_subjectivity = 0

    def compute_sentiment(self, opinion):
        blob = TextBlob(opinion)
        self.total_polarity += blob.sentiment.polarity
        self.total_subjectivity += blob.sentiment.subjectivity

    def get_sentiment(self, data_length):
        average_polarity = self.total_polarity / data_length
        average_subjectivity = self.total_subjectivity / data_length

        if average_polarity > 0:
            overall_sentiment = "Positive"
        elif average_polarity < 0:
            overall_sentiment = "Negative"
        else:
            overall_sentiment = "Neutral"

        return {'average_polarity': average_polarity, 'average_subjectivity': average_subjectivity, 'overall_sentiment': overall_sentiment}



# # Load the JSON file containing the reviews
# with open('./data/reviews_pakket.json', 'r', encoding="utf8") as f:
#     data = json.load(f)

# # Extract the opinions from the data and calculate the average polarity and subjectivity scores
# total_polarity = 0
# total_subjectivity = 0
# #for item in data:
#     #opinion = item['opinion']
#     #blob = TextBlob(opinion)
#     #total_polarity += blob.sentiment.polarity
#     #total_subjectivity += blob.sentiment.subjectivity
# def get_sentiment(opinion):
# blob = TextBlob(opinion)
# total_polarity += blob.sentiment.polarity
# total_subjectivity += blob.sentiment.subjectivity
# average_polarity = total_polarity / len(data)
# average_subjectivity = total_subjectivity / len(data)

# # Determine the overall sentiment and subjectivity based on the average polarity and subjectivity scores
# if average_polarity > 0:
#     overall_sentiment = "Positive"
# elif average_polarity < 0:
#     overall_sentiment = "Negative"
# else:
#     overall_sentiment = "Neutral"

# if average_subjectivity > 0.5:
#     overall_subjectivity = "Subjective"
# else:
#     overall_subjectivity = "Objective"

# # Print the overall sentiment and subjectivity and the average polarity and subjectivity scores
# print("Overall sentiment: ", overall_sentiment)
# print("Overall subjectivity: ", overall_subjectivity)
# print("Average polarity: ", average_polarity)
# print("Average subjectivity: ", average_subjectivity)