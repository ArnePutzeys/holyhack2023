# input is een lijst van woorden en elk woord van deze lijst wordt per record vd json gecheckt of het erin zit
# alle scores adden en dan delen door het aantal voorkomens dat geteld is
# data afhankelijkheid dus load_data moet aangepast worden zodat je kan kiezen welke data je wilt laden in bepaalde tijdspanne
from data_load import data_load, data_load2, data_load4
from sentiment_dutch import Sentiment_dutch
from sentiment_analysis2 import Sentiment
import time

def count(input, file, startdate=None, enddate=None, lines=None):
    """This is a function that counts the amount of times a string in input is in the total file or 
       in the file where date is between startdate and enddate or the maximal number of lines == lines

    Args:
        input (list(string)): in this list are the strings which are checked and counted in this function
        file (string): path where the json is situated in a string
        startdate (string, optional): The startdate in the format YYYY-MM-DD. Defaults to None.
        enddate (string, optional): The enddate in the format YYY-MM-DD. Defaults to None.
        lines (string, optional): amount of lines you want to read from json file. Defaults to None.

    Returns:
        list of lists: keywords,totaal,procent,polariteit,subjectivity,gem_review,tijdsvoorkomen, x_values, y_values
                        Every element is a list in the big return list
    """
    english = False
    # enige nederlandse file dus nederlands getraind Sentiment model nodig
    if file.endswith('reviews_pakket.json'):
        count = {element: [0, 0, Sentiment_dutch(), [], []] for element in input}
    else:
        # Engels getraind Sentiment model nodig
        english = True
        count = {element: [0, 0, Sentiment(), [], []] for element in input}

    # acquiring values
    start_time = time.time()
    start_time_tot = time.time()
    graph_values = dict()
    # Check for start and end date and load data accordingly
    if startdate != None and enddate != None:
        # If lines is None, load all data
        if lines == None:
            sentences, score, iterations, graph_values = data_load2(file, ['opinion', 'score'], startdate, enddate, lines)
        # If lines is specified, load that many lines of data
        else:
            sentences, score, iterations, graph_values = data_load2(file, ['opinion', 'score'], startdate, enddate, 0)
    # If start and end date are not specified, load data with data_load4
    else:
        # If lines is None, load all data
        if lines == None:
            sentences, score, iterations, graph_values = data_load4(file, ['opinion', 'score'], None,None, 0, input)
        else:
            # If lines is specified, load that many lines of data
            sentences, score, iterations, graph_values = data_load4(file, ['opinion', 'score'], None,None, lines,input)
    end_time = time.time()
    print("elapsed time: "+str(end_time-start_time))
    start_time = time.time()
    total_limit = 0
    # Loop through each sentence and each word in input
    for i in range(len(sentences)):
        for word in input:
            if word in sentences[i].lower():
                count[word][0] += 1
                count[word][1] += int(score[i])
                if total_limit < 100:
                    count[word][2].compute_sentiment(sentences[i])
                    total_limit += 1
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
    # iterate over every element in the keys of our count dictionary
    # because of calculations which can be zero when there are no matches found they all need to be in
    # a try and except keyboard
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
    # initialising x_values en y_values
    x_values = []
    y_values = []
    # calculate x_values and y_values while iterating over the length of count
    for i in range(len(count)):
        procent.append(totaal[i]/iterations)
        x_values.append([])
        y_values.append([])
        for element in graph_values:
            x_values[i].append(element)
            y_values[i].append(graph_values[element])

    # (keywords), hoe_vaak_totaal, hoe_vaak_procent, polariteit, (subjectiviteit), gem_review, tijdsvoorkomen
    # print(keywords,totaal,procent,polariteit,subjectivity,gem_review,tijdsvoorkomen,x_values,y_values)
    return keywords,totaal,procent,polariteit,subjectivity,gem_review,tijdsvoorkomen, x_values, y_values
     
# testing purposes       
if __name__ == "__main__":
    input = ['status','quit']
    #input = ['Vinted-app', 'verzending', 'bezorging', 'post', 'levering', 'opruimen', 'Pakket']
    #input = ['quality']
    for i in range(len(input)):
        input[i] = input[i].lower()

    file = '../../data/reviews_pakket.json'
    #file = '../../data/spotify.json'
    count(input, file,None,None,20000)
    #count(input, file, '2020-11-19', '2022-12-30')