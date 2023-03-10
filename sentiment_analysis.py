import nltk, json
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the Vader lexicon if not already downloaded
nltk.download('vader_lexicon')

# Define the reviews as a list
reviews = [
    "This restaurant was amazing! The food was delicious and the service was excellent.",
    "I was very disappointed with my experience at this hotel. The room was dirty and the staff was unfriendly.",
    "I loved the movie! The acting was superb and the story was so engaging.",
    "The product was defective and the company's customer service was unhelpful. I do not recommend this product.",
    "The concert was incredible! The band played all their hits and the atmosphere was electric."
]

with open('./data/reviews_pakket.json', 'r', encoding="utf8") as f:
    data = json.load(f)

#reviews = []
#for item in data:
 #   opinion = item['opinion']

# Instantiate the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Calculate the sentiment score for all reviews together
total_sentiment_score = 0
for item in data:
    review = item['opinion']
    sentiment_score = analyzer.polarity_scores(review)['compound']
    total_sentiment_score += sentiment_score
    
total_sentiment_score = total_sentiment_score / len(data)

# Determine the overall sentiment based on the total sentiment score
if total_sentiment_score > 0:
    overall_sentiment = "Positive"
elif total_sentiment_score < 0:
    overall_sentiment = "Negative"
else:
    overall_sentiment = "Neutral"

# Print the overall sentiment and total sentiment score
print("Overall sentiment: ", overall_sentiment)
print("Total sentiment score: ", total_sentiment_score)
