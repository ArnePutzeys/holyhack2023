import os
import openai
from time import sleep
from data_load import data_load
from pprint import pprint
from gensim import corpora, models
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import nltk

example_file = r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json'

# Currently supported languages: 'English' and 'Dutch'
def get_subjects(file_path, language):

    nltk.download('stopwords')

    # Load dataset
    reviews = data_load(file_path, 'opinion', None, None, 5)[0]

    #language = language.lower()
    #print(language)
    #if language != 'dutch' or language != 'english':
    #    print('Error: unsupported language for classification')
    #    exit()

    # Tokenize words and remove stopwords
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = set(stopwords.words(language))


    def tokenize(text):
        return [word.lower() for word in tokenizer.tokenize(text) if word.lower() not in stop_words]


    tokens_list = [tokenize(review) for review in reviews]

    # Create dictionary and corpus
    dictionary = corpora.Dictionary(tokens_list)
    corpus = [dictionary.doc2bow(tokens) for tokens in tokens_list]

    # Run LDA
    lda_model = models.LdaModel(
        corpus=corpus, id2word=dictionary, num_topics=10, passes=15)


    # pprint(lda_model.print_topics())
    # Print topics and their keywords

    # Set up OpenAI API credentials
    openai.api_key = "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"


    output = dict()
    for i, topic in lda_model.show_topics(formatted=True, num_topics=10, num_words=15):
        # print(f"Topic {i+1}:")
        keywords = [word.split("*")[1].replace('"', '')
                    for word in topic.split(" + ")]
        prompt = "Find the subject name that the following words have in common " + \
            ", ".join(keywords) + \
            ". Please only type the subject without any extra text."
        sleep(4)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        subjects = response.choices[0].text.replace('\n', '').replace('"', '').split()[-1]
        print(subjects)
        output[subjects] = keywords

        #print(f"Subject: {response.choices[0].text}")
        #print(f"Top keywords: {keywords}\n")

    return output
