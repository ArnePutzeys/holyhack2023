import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from gensim import corpora, models
from pprint import pprint
from data_load import data_load
import openai
import os

# Load dataset
reviews = data_load(r'C:\Users\kjell\Downloads\holyhack\spotify_data.json', 'opinion')

#reviews = ["This product is amazing! It exceeded my expectations and I would highly recommend it to anyone looking for a high-quality product.", 
#           "I was disappointed with this product. It didn't work as advertised and I ended up returning it.",
#           "Great customer service! The support team was very helpful and responsive to my questions.",
#           "This is the best restaurant in town. The food is always delicious and the service is top-notch.",
#           "I had a terrible experience at this hotel. The room was dirty and the staff was rude and unhelpful.",
#           "The shipping was fast and the product arrived in perfect condition. I would definitely order from this company again.",
#           "The movie was entertaining but predictable. I wouldn't say it's a must-see, but it's worth watching if you have some free time.",
#           "I love this app! It's so easy to use and has all the features I need to manage my tasks.",
#           "The concert was amazing! The performer was incredibly talented and put on a great show.",
#           "I had high hopes for this book, but I found it to be quite boring and uninteresting."]


# Tokenize words and remove stopwords
tokenizer = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))

def tokenize(text):
    return [word.lower() for word in tokenizer.tokenize(text) if word.lower() not in stop_words]

tokens_list = [tokenize(review) for review in reviews]

# Create dictionary and corpus
dictionary = corpora.Dictionary(tokens_list)
corpus = [dictionary.doc2bow(tokens) for tokens in tokens_list]

# Run LDA
lda_model = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=10)


#pprint(lda_model.print_topics())
# Print topics and their keywords

# Set up OpenAI API credentials
openai.api_key = "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"

for i, topic in lda_model.show_topics(formatted=True, num_topics=5, num_words=10):
    #print(f"Topic {i+1}:")
    keywords = [word.split("*")[1].replace('"', '') for word in topic.split(" + ")]
    prompt = "Find the subject name that the following words have in common " + ", ".join(keywords) + ". Please only type the subject without any extra text."

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )

    print(f"Subject: {response.choices[0].text}")
    print(f"Top keywords: {keywords}\n")

