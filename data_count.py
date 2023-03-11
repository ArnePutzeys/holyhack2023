# input is een lijst van woorden en elk woord van deze lijst wordt per record vd json gecheckt of het erin zit
# alle scores adden en dan delen door het aantal voorkomens dat geteld is
# data afhankelijkheid dus load_data moet aangepast worden zodat je kan kiezen welke data je wilt laden in bepaalde tijdspanne
from data_load import data_load
from sentiment_dutch import Sentiment_dutch
from sentiment_analysis2 import Sentiment

def count(input, file, startdate=None, enddate=None):
    iterations = 0
    count = {element: [0, 0, Sentiment_dutch()] for element in input}

    sentences, iterations = data_load(file, 'opinion', startdate, enddate)
    score, iterations = data_load(file, 'score', startdate, enddate)

    for i in range(len(sentences)):
        for word in input:
            if word in sentences[i].lower():
                count[word][0] += 1
                count[word][1] += int(score[i])
                count[word][2].compute_sentiment(sentences[i])
        print("it: "+str(i))
                
    for element in count.keys():
        count[element][1] = count[element][1] / count[element][0]
    print(count)
    print(count[element][2].get_sentiment(count[element][0]))
            
if __name__ == "__main__":
    input = ['slecht']
    #input = ['quality']
    for i in range(len(input)):
        input[i] = input[i].lower()

    file = 'data/reviews_pakket.json'
    #file = 'data/reviews_spotify.csv'
    count(input, file)
    #count(input, file, '2020-11-19', '2020-12-30')