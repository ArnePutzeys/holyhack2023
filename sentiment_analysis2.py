import json
from textblob import TextBlob

# Load the JSON dataset into a Pandas DataFrame
#df = pd.read_json('./data/reviews_pakket.json')

# Load the JSON file containing the reviews
with open('./data/reviews_pakket.json', 'r', encoding="utf8") as f:
    data = json.load(f)

# Extract the opinions from the data and calculate the average polarity and subjectivity scores
total_polarity = 0
total_subjectivity = 0
for item in data:
    opinion = item['opinion']
    blob = TextBlob(opinion)
    total_polarity += blob.sentiment.polarity
    total_subjectivity += blob.sentiment.subjectivity

average_polarity = total_polarity / len(data)
average_subjectivity = total_subjectivity / len(data)

# Determine the overall sentiment and subjectivity based on the average polarity and subjectivity scores
if average_polarity > 0:
    overall_sentiment = "Positive"
elif average_polarity < 0:
    overall_sentiment = "Negative"
else:
    overall_sentiment = "Neutral"

if average_subjectivity > 0.5:
    overall_subjectivity = "Subjective"
else:
    overall_subjectivity = "Objective"

# Print the overall sentiment and subjectivity and the average polarity and subjectivity scores
print("Overall sentiment: ", overall_sentiment)
print("Overall subjectivity: ", overall_subjectivity)
print("Average polarity: ", average_polarity)
print("Average subjectivity: ", average_subjectivity)