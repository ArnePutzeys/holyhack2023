# input is een lijst van woorden en elk woord van deze lijst wordt per record vd json gecheckt of het erin zit
# alle scores adden en dan delen door het aantal voorkomens dat geteld is
# data afhankelijkheid dus load_data moet aangepast worden zodat je kan kiezen welke data je wilt laden in bepaalde tijdspanne
from data_load import data_load, data_load2, data_load3, data_load4
from sentiment_dutch import Sentiment_dutch
from sentiment_analysis2 import Sentiment
from multiprocessing import Process, Queue
import multiprocessing
import numpy as np
import time

def count(input, file, startdate=None, enddate=None, lines=None):
    #count = {element: [0, 0, Sentiment_dutch()] for element in input}
    if file.endswith('reviews_pakket.json'):
        count = {element: [0, 0, Sentiment_dutch()] for element in input}
    else:
        count = {element: [0, 0, Sentiment()] for element in input}

    start_time = time.time()
    start_time_tot = time.time()
    if startdate != None and enddate != None:
        if lines == None:
            sentences, score, iterations = data_load2(file, ['opinion', 'score'], startdate, enddate, lines)
        else:
            sentences, score, iterations = data_load2(file, ['opinion', 'score'], startdate, enddate, 0)
    else:
        if lines == None:
            sentences, score, iterations = data_load4(file, ['opinion', 'score'], None,None, 0, input)
        else:
            sentences, score, iterations = data_load4(file, ['opinion', 'score'], None,None, lines,input)
    end_time = time.time()
    print("elapsed time: "+str(end_time-start_time))
    start_time = time.time()
    total_limit = 0
    for i in range(len(sentences)):
        for word in input:
            if word in sentences[i].lower():
                count[word][0] += 1
                count[word][1] += int(score[i])
                if total_limit < 100:
                    count[word][2].compute_sentiment(sentences[i])
                    total_limit += 1
        #print("it2: "+str(i))
    end_time = time.time()
    print("elapsed time: "+str(end_time-start_time))
    end_time_tot= time.time()
    print("elapsed time tot: "+str(end_time_tot-start_time_tot))

    keywords = input
    tijdsvoorkomen = []
    totaal = []
    procent = []
    polariteit = []
    sentiment = []
    gem_review = []
    for element in count.keys():
        try: 
            count[element][1] = count[element][1] / count[element][0]
            keywords = input
            totaal = [count[element][0] for element in count]
            procent = [t / iterations for t in totaal]
            polariteit = [count[element][2].get_sentiment(t)['average_polarity'] for element, t in zip(count, totaal)]
            sentiment = [count[element][2].get_sentiment(t)['overall_sentiment'] for element, t in zip(count, totaal)]
            gem_review = [count[element][1] for element in count]
            tijdsvoorkomen = []
        except ZeroDivisionError:
            count[element][1] = 0 
        try:
            totaal = [count[element][0] for element in count]
        except ZeroDivisionError:
            totaal.append(0)
        try:
            procent = [t / iterations for t in totaal]
        except ZeroDivisionError:
            procent.append(0)
        try:
            polariteit = [count[element][2].get_sentiment(t)['average_polarity'] for element, t in zip(count, totaal)]
        except ZeroDivisionError:
            polariteit.append(0)
        try:    
            sentiment = [count[element][2].get_sentiment(t)['overall_sentiment'] for element, t in zip(count, totaal)]
        except ZeroDivisionError:
            sentiment.append(0)
        try:
            gem_review = [count[element][1] for element in count]
        except ZeroDivisionError:
            gem_review.append(0)

    # (keywords), hoe_vaak_totaal, hoe_vaak_procent, polariteit, (subjectiviteit), gem_review, tijdsvoorkomen
    print(keywords,totaal,procent,polariteit,sentiment,gem_review,tijdsvoorkomen)
    return keywords,totaal,procent,polariteit,sentiment,gem_review,tijdsvoorkomen
            
if __name__ == "__main__":
    input = ['status', 'quit']
    #input = ['quality']
    for i in range(len(input)):
        input[i] = input[i].lower()

    file = '../../data/reviews_pakket.json'
    #file = 'data/reviews_spotify.csv'
    count(input, file,None,None,10000)
    #count(input, file, '2020-11-19', '2020-12-30')