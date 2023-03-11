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

def count(input, file, startdate=None, enddate=None):
    count = {element: [0, 0, Sentiment_dutch()] for element in input}

    # sentences = data_load(file, 'opinion', startdate, enddate)
    # score = data_load(file, 'score', startdate, enddate)
    
    start_time = time.time()
    # path, argument, output, score, start=0, end=None)
    sentences, score, iterations = data_load2(file, ['opinion', 'score'], [], [], startdate, enddate)
    end_time = time.time()
    print("elapsed time: "+str(end_time-start_time))
    
    # multiprocessing
    
    # chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    # pool = multiprocessing.Pool(processes=5)
    # results = pool.map(process_chunk, chunks)
    
    for i in range(len(sentences)):
        for word in input:
            if word in sentences[i].lower():
                count[word][0] += 1
                count[word][1] += int(score[i])
                count[word][2].compute_sentiment(sentences[i])
        print("it2: "+str(i))
                
    for element in count.keys():
        count[element][1] = count[element][1] / count[element][0]
    # print(count)
    # print(count[element][2].get_sentiment(count[element][0]))
    # (keywords), hoe_vaak_totaal, hoe_vaak_procent, polariteit, (subjectiviteit), gem_review, tijdsvoorkomen
    keywords = input
    # totaal = [count[element][0] for element in count.keys()]
    # procent = [totaal[i]/iterations for i in range(len(count))]
    # polariteit = [count[element][2].get_sentiment(count[element][0])['average_polarity'] for element in count.keys()]
    # sentiment = [count[element][2].get_sentiment(count[element][0])['overall_sentiment'] for element in count.keys()]
    # gem_review = [count[element][1] for element in count.keys()]
    
    totaal = [count[element][0] for element in count]
    procent = [t / iterations for t in totaal]
    polariteit = [count[element][2].get_sentiment(t)['average_polarity'] for element, t in zip(count, totaal)]
    sentiment = [count[element][2].get_sentiment(t)['overall_sentiment'] for element, t in zip(count, totaal)]
    gem_review = [count[element][1] for element in count]
    tijdsvoorkomen = []
    #print(keywords,totaal,procent,polariteit,sentiment,gem_review,tijdsvoorkomen)
    return keywords,totaal,procent,polariteit,sentiment,gem_review,tijdsvoorkomen
            
if __name__ == "__main__":
    input = ['status']
    #input = ['quality']
    for i in range(len(input)):
        input[i] = input[i].lower()

    file = 'data/reviews_pakket.json'
    #file = 'data/reviews_spotify.csv'
    count(input, file)
    #count(input, file, '2020-11-19', '2020-12-30')