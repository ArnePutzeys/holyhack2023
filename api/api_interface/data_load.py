import json
import csv
import numpy as np


def get_date(date):
    return date.split('T')[0][1:].split('-')


def data_load(path, argument, startdate=None, enddate=None, number_of_reviews=0):
    if startdate != None:
        startdate = startdate.split('-')
    if enddate != None:
        enddate = enddate.split('-')
    output = []
    
    # Opening JSON file
    f = open(path, 'r', encoding='utf-8')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    k = 1
    for i in data:
        if startdate != None and enddate != None:
            review_date = get_date(i['date'])
        if argument == 'opinion':
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
        elif startdate != None and enddate != None and review_date[0] == enddate[0] and review_date[1] == enddate[1] and review_date[2] < enddate[2]:
            print(startdate, review_date, enddate)
            break
        #print("it: "+str(k))
        k += 1
    # Closing file
    f.close()
    return output

def data_load2(path, argument, startdate=None, enddate=None, number_of_reviews=0):
    if startdate != None:
        startdate = startdate.split('-')
    if enddate != None:
        enddate = enddate.split('-')
    output = []
    score = []
    
    # Opening JSON file
    f = open(path, 'r', encoding='utf-8')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    k = 1
    for i in data:
        if startdate != None and enddate != None:
            review_date = get_date(i['date'])
        if 'opinion' in argument:
            if startdate == None and enddate == None:
                output.append(i['opinion']+i['title'])
                score.append(i['score'])
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                output.append(i['opinion']+i['title'])
                score.append(i['score'])
        elif 'title' in argument:
            if startdate == None and enddate == None:
                output.append(i['title']+i['opinion'])
                score.append(i['score'])
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                output.append(i['title']+i['opinion'])
                score.append(i['score'])
        else:
            if startdate == None and enddate == None:
                output.append(i[argument[0]])
                score.append(i[argument[1]])
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                print("found")
                output.append(i[argument][0])
                score.append(i[argument[1]])

        if k == number_of_reviews and number_of_reviews != 0:
            break
        elif k == len(data) and number_of_reviews == 0:
            break
        elif startdate != None and enddate != None and review_date[0] == enddate[0] and review_date[1] == enddate[1] and review_date[2] < enddate[2]:
            print(startdate, review_date, enddate)
            break
        #print("it: "+str(k))
        k += 1
    # Closing file
    f.close()
    return output, score, k


def data_load3(path, argument, output, score, start, end):
    
    # Opening JSON file
    f = open(path, 'r', encoding='utf-8')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    start = 0
    end = len(data)
    
    if end == 0 or end > len(data):
        end = len(data)
            
    # Iterating through the json
    # list
    k = 0
    for i in range(start,end):
        if 'opinion' in argument:
            output.append(data[i]['opinion']+data[i]['title'])
            score.append(data[i]['score'])
        elif 'title' in argument:
            output.append(data[i]['title']+data[i]['opinion'])
            score.append(data[i]['score'])
        else:
            output.append(data[i][argument[0]])
            score.append(data[i][argument[1]])
                
        if k == end:
            break
        #print("it: "+str(k))
        k += 1
    # Closing file
    f.close()
    return output, score

def data_load4(path, argument, startdate=None, enddate=None, number_of_reviews=0, input=[]):
    if startdate != None:
        startdate = startdate.split('-')
    if enddate != None:
        enddate = enddate.split('-')
    output = []
    score = []
    
    # Opening JSON file
    f = open(path, 'r', encoding='utf-8')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    k = 1
    
    input1 = {string.lower() for string in input}
    for i in data:
        if startdate != None and enddate != None:
            review_date = get_date(i['date'])
        if 'opinion' in argument:
            out = set((i['opinion']+i['title']).split(' '))
            out = {string.lower().strip('.,!;:()[]{}?/\\\'\"') for string in out}
            if startdate == None and enddate == None and (out & input1):
                output.append(i['opinion']+i['title'])
                score.append(i['score'])
            elif startdate != None and enddate != None and startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2] and (out & input1):
                output.append(i['opinion']+i['title'])
                score.append(i['score'])
        elif 'title' in argument:
            out = set((i['title']+i['opinion']).split(' '))
            out = {string.lower().strip('.,!;:()[]{}?/\\\'\"') for string in out}
            if startdate == None and enddate == None and (out & input1):
                output.append(i['title']+i['opinion'])
                score.append(i['score'])
            elif startdate != None and enddate != None and startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2] and (out & input1):
                output.append(i['title']+i['opinion'])
                score.append(i['score'])
        else:
            out = set(i[argument[0]].split(' '))
            out = {string.lower().strip('.,!;:()[]{}?/\\\'\"') for string in out}
            if startdate == None and enddate == None and (out & input1):
                output.append(i[argument[0]])
                score.append(i[argument[1]])
            elif startdate != None and enddate != None and startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2] and (out & input1):
                print("found")
                output.append(i[argument][0])
                score.append(i[argument[1]])

        if k == number_of_reviews and number_of_reviews != 0:
            break
        elif k == len(data) and number_of_reviews == 0:
            break
        elif startdate != None and enddate != None and review_date[0] == enddate[0] and review_date[1] == enddate[1] and review_date[2] < enddate[2]:
            print(startdate, review_date, enddate)
            break
        #print("it: "+str(k))
        k += 1
    # Closing file
    f.close()
    return output, score, k