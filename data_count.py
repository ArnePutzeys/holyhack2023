# input is een lijst van woorden en elk woord van deze lijst wordt per record vd json gecheckt of het erin zit
# alle scores adden en dan delen door het aantal voorkomens dat geteld is
# data afhankelijkheid dus load_data moet aangepast worden zodat je kan kiezen welke data je wilt laden in bepaalde tijdspanne
from data_load import data_load

def count(input, file, startdate=None, enddate=None):
    count = dict()
    for element in input:
        count[element] = [0,0]
    sentences = data_load(file, 'opinion', startdate, enddate)
    score = data_load(file, 'score', startdate, enddate)

    for i in range(len(sentences)):
        for word in input:
            if word in sentences[i].lower():
                count[word][0] += 1
                count[word][1] += int(score[i])
                
    for element in count.keys():
        count[element][1] = count[element][1] / count[element][0]
    print(count)
            
if __name__ == "__main__":
    input = ['Pakket','status']
    for i in range(len(input)):
        input[i] = input[i].lower()

    file = 'data/reviews_pakket.json'
    count(input, file)
    count(input, file, '2020-11-19', '2020-11-20')