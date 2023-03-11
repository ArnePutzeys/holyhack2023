# input is een lijst van woorden en elk woord van deze lijst wordt per record vd json gecheckt of het erin zit
# alle scores adden en dan delen door het aantal voorkomens dat geteld is
# data afhankelijkheid dus load_data moet aangepast worden zodat je kan kiezen welke data je wilt laden in bepaalde tijdspanne
from data_load import data_load, data_load2, data_load3, data_load4
from sentiment_dutch import Sentiment_dutch
from sentiment_analysis2 import Sentiment
import time

def count(input, file, startdate=None, enddate=None, lines=None):
    english = False
    #count = {element: [0, 0, Sentiment_dutch()] for element in input}
    if file.endswith('reviews_pakket.json'):
        count = {element: [0, 0, Sentiment_dutch(), [], []] for element in input}
    else:
        english = True
        count = {element: [0, 0, Sentiment(), [], []] for element in input}

    start_time = time.time()
    start_time_tot = time.time()
    graph_values = dict()
    if startdate != None and enddate != None:
        if lines == None:
            sentences, score, iterations, graph_values = data_load2(file, ['opinion', 'score'], startdate, enddate, lines)
        else:
            sentences, score, iterations, graph_values = data_load2(file, ['opinion', 'score'], startdate, enddate, 0)
    else:
        if lines == None:
            sentences, score, iterations, graph_values = data_load4(file, ['opinion', 'score'], None,None, 0, input)
        else:
            sentences, score, iterations, graph_values = data_load4(file, ['opinion', 'score'], None,None, lines,input)
    end_time = time.time()
    print("elapsed time: "+str(end_time-start_time))
    start_time = time.time()
    total_limit = 0
    for i in range(len(sentences)):
        for word in input:
            if word in sentences[i].lower():
                count[word][0] += 1
                # print(count[word][1])
                # print(score[i])
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
    subjectivity = []
    gem_review = []

    for element in count.keys():
        totaal.append(count[element][0])
        try:
            polariteit.append(count[element][2].get_sentiment(count[element][0])['average_polarity'])
        except ZeroDivisionError:
            polariteit.append(0)
        try:
            if english:
                subjectivity.append(count[element][2].get_sentiment(count[element][0])['average_subjectivity'])
            else:
                subjectivity.append(0)
        except ZeroDivisionError:
            subjectivity.append(0)
        try:
            gem_review.append(count[element][1]/count[element][0])
        except ZeroDivisionError:
            gem_review.append(0)

    for i in range(len(count)):
        procent.append(totaal[i]/iterations)
        
        x_values = []
        y_values = []
        for element in graph_values:
            x_values.append(element)
            y_values.append(graph_values[element])

    # (keywords), hoe_vaak_totaal, hoe_vaak_procent, polariteit, (subjectiviteit), gem_review, tijdsvoorkomen
    print(keywords,totaal,procent,polariteit,subjectivity,gem_review,tijdsvoorkomen,x_values,y_values)
    return keywords,totaal,procent,polariteit,subjectivity,gem_review,tijdsvoorkomen, x_values, y_values
            
if __name__ == "__main__":
    input = ['status','quit']
    #input = ['Vinted-app', 'verzending', 'bezorging', 'post', 'levering', 'opruimen', 'Pakket']
    #input = ['quality']
    for i in range(len(input)):
        input[i] = input[i].lower()

    file = '../../data/reviews_pakket.json'
    #file = '../../data/spotify_data.json'
    count(input, file,None,None,20000)
    #count(input, file, '2020-11-19', '2022-12-30')