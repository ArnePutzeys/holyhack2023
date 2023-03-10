import json

def get_date(date):
    return date.split('T')[0][1:].split('-')

def data_load(path, argument, startdate=None, enddate=None, number_of_reviews=0):
    if startdate != None:
        startdate = startdate.split('-')
    if enddate != None:
        enddate = enddate.split('-')
    output = []
    # Opening JSON file
    f = open(path, 'r')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    k = 0
    for i in data:
        if startdate != None and enddate != None:
            review_date = get_date(i['date'])
        if argument =='opinion':
            if startdate == None and enddate == None:
                output.append(i[argument]+i['title'])
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                output.append(i[argument]+i['title'])    
        elif argument == 'title':
            if startdate == None and enddate == None:
                output.append(i[argument]+i['opinion'])
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                output.append(i[argument]+i['opinion'])
        else:
            if startdate == None and enddate == None:
                output.append(i[argument])
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                output.append(i[argument])

        if k == number_of_reviews and number_of_reviews != 0:
            break
        elif k == len(data) and number_of_reviews == 0:
            break
        k += 1
    
    # Closing file
    f.close()
    return output