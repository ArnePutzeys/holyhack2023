import json
import numpy as np
import datetime


def get_date(date):
    """Get the date splitted in a list from the date string

    Args:
        date (string): string of the date in format YYYY-MM-DD

    Returns:
        list: A list of the date splitted in year [0], month [1] and day [2]
    """
    if date.startswith('\"'):
        return date.split('T')[0][1:].split('-')
    else:
        return date.split('T')[0].split('-')


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
    """This function is designed to load data between a start and enddate or a number of lines

    Args:
        path (string): string of the path to the json file to load data from
        argument (list[string]): List of strings of the arguments to check for in the json file
        startdate (string, optional): The startdate in the format YYYY-MM-DD. Defaults to None.
        enddate (string, optional): The enddate in the format YYY-MM-DD. Defaults to None.
        number_of_reviews (int, optional): amount of lines you want to read from json file. Defaults to 0.
        input (list, optional): list where the input stands in. Defaults to [].

    Returns:
        nested lists: list(output, score, k, graph_values) where output, score, k, graph_values
        are lists on its own.
    """
    if startdate != None:
        startdate = startdate.split('-')
    if enddate != None:
        enddate = enddate.split('-')
    output = []
    score = []
    graph_values = dict()
    graph_date = str()
    
    # Opening JSON file
    f = open(path, 'r', encoding='utf-8')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    k = 1
    # Loop through the data
    for i in data:
        # Check if startdate and enddate are provided
        if startdate != None and enddate != None:
            # Get the date from the review and format it for the graph
            review_date = get_date(i['date'])
            graph_date = "-".join(review_date)
        else:
            # Get the date from the review
            review_date = get_date(i['date'])
            # Check if the review is from the last year
            if int(review_date[0]) >= datetime.datetime.now().year - 1:
                # Format the date for the graph
                graph_date = "-".join(review_date)
        # Check if 'opinion' is in the argument
        if 'opinion' in argument:
            # Check if startdate and enddate are not provided
            if startdate == None and enddate == None:
                # Add the opinion and title to the output list
                output.append(i['opinion']+i['title'])
                # Add the score to the score list
                score.append(i['score'])
                # Update the graph values
                if graph_date in graph_values.keys():
                    graph_values[graph_date] += 1
                else:
                    graph_values[graph_date] = 1
            # Check if the review date is within the provided date range
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                # Add the opinion and title to the output list
                output.append(i['opinion']+i['title'])
                # Add the score to the score list
                score.append(i['score'])
                # Update the graph values
                if graph_date in graph_values.keys():
                    graph_values[graph_date] += 1
                else:
                    graph_values[graph_date] = 1
        # Check if 'title' is in the argument
        elif 'title' in argument:
            # Check if startdate and enddate are not provided
            if startdate == None and enddate == None:
                # Add the title and opinion to the output list
                output.append(i['title']+i['opinion'])
                # Add the score to the score list
                score.append(i['score'])
                # Update the graph values
                if graph_date in graph_values.keys():
                    graph_values[graph_date] += 1
                else:
                    graph_values[graph_date] = 1
            # Check if the review date is within the provided date range
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                # Add the title and opinion to the output list
                output.append(i['title']+i['opinion'])
                # Add the score to the score list
                score.append(i['score'])
                # Update the graph values
                if graph_date in graph_values.keys():
                    graph_values[graph_date] += 1
                else:
                    graph_values[graph_values] = 1
        else:
            # This block of code checks if the start and end date are not specified.
            if startdate == None and enddate == None:
                # If so, append the first element of the 'argument' list to the 'output' list
                # and the second element to the 'score' list.
                output.append(i[argument[0]])
                score.append(i[argument[1]])
                # Check if 'graph_date' exists in the 'graph_values' dictionary.
                if graph_date in graph_values.keys():
                    # If it does, increment the value corresponding to 'graph_date' by 1.
                    graph_values[graph_date] += 1
                else:
                    # Otherwise, add 'graph_date' to the 'graph_values' dictionary with a value of 1.
                    graph_values[graph_date] = 1
            # This block of code checks if the review date falls within the specified range.
            elif startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2]:
                # If the review date falls within the specified range, check if 'graph_date' exists in the 'graph_values' dictionary.
                if graph_date in graph_values.keys():
                    # If it does, increment the value corresponding to 'graph_date' by 1.
                    graph_values[graph_date] += 1
                else:
                    # Otherwise, add 'graph_date' to the 'graph_values' dictionary with a value of 1.
                    graph_values[graph_date] = 1
                # Append the first element of the 'argument' list to the 'output' list and the second element to the 'score' list.
                output.append(i[argument][0])
                score.append(i[argument[1]])

            # This block of code checks if the number of reviews has been reached or if all reviews have been processed.
            if k == number_of_reviews and number_of_reviews != 0:
                # If the number of reviews has been reached and it is not 0, break out of the loop.
                break
            elif k == len(data) and number_of_reviews == 0:
                # If all reviews have been processed and the number of reviews is 0, break out of the loop.
                break
            # This block of code checks if the review date is equal to the end date.
            elif startdate != None and enddate != None and review_date[0] == enddate[0] and review_date[1] == enddate[1] and review_date[2] < enddate[2]:
                # If the review date is equal to the end date, print the start date, review date, and end date and break out of the loop.
                print(startdate, review_date, enddate)
                break
        k += 1
    # Closing file
    f.close()
    return output, score, k, graph_values


def data_load4(path, argument, startdate=None, enddate=None, number_of_reviews=0, input=[]):
    """This function loads data specifically for the whole dataset. The data is only handled for dates
    between the startdate and enddate. If no startdate or enddate is given, the data is loaded for every combination

    Args:
        path (string): string of the path to the json file to load data from
        argument (list[string]): List of strings of the arguments to check for in the json file
        startdate (string, optional): The startdate in the format YYYY-MM-DD. Defaults to None.
        enddate (string, optional): The enddate in the format YYY-MM-DD. Defaults to None.
        number_of_reviews (int, optional): amount of lines you want to read from json file. Defaults to 0.
        input (list, optional): list where the input stands in. Defaults to [].

    Returns:
        nested lists: list(output, score, k, graph_values) where output, score, k, graph_values
        are lists on its own.
    """
    
    # split startdate and enddate in ['YYYY','MM','DD']
    if startdate != None:
        startdate = startdate.split('-')
    if enddate != None:
        enddate = enddate.split('-')
    # initialization
    output = []
    score = []
    graph_values = dict()
    graph_date = None
    
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
            graph_date = "-".join(review_date)
        else:
            review_date = get_date(i['date'])
            if int(review_date[0]) >= datetime.datetime.now().year - 1:
                graph_date = "-".join(review_date)
        # Checking if 'opinion' is in the argument and creating a set of words from the 'opinion' and 'title' fields
        if 'opinion' in argument:
            out = set((i['opinion']+i['title']).split(' '))
            out = {string.lower().strip('.,!;:()[]{}?/\\\'\"') for string in out}

            # If startdate and enddate are not specified, append output, score, and update graph_values if graph_date exists
            if startdate == None and enddate == None and (out & input1):
                output.append(i['opinion']+i['title'])
                score.append(i['score'])
                if graph_date in graph_values.keys() and graph_date != None:
                    graph_values[graph_date] += 1
                elif graph_date != None:
                    graph_values[graph_date] = 1
            
            # If startdate and enddate are specified, append output, score, and update graph_values if graph_date exists
            elif startdate != None and enddate != None and startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2] and (out & input1):
                output.append(i['opinion']+i['title'])
                score.append(i['score'])
                if graph_date in graph_values.keys() and graph_date != None:
                    graph_values[graph_date] += 1
                elif graph_date != None:
                    graph_values[graph_date] = 1
            # If startdate and enddate are not specified, append output, score, and update graph_values if graph_date exists
            elif startdate != None and enddate != None and startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2] and (out & input1):
                output.append(i['title']+i['opinion'])
                score.append(i['score'])
                if graph_date in graph_values.keys() and graph_date != None:
                    graph_values[graph_date] += 1
                elif graph_date != None:
                    graph_values[graph_date] = 1
        else:
            out = set(i[argument[0]].split(' '))
            out = {string.lower().strip('.,!;:()[]{}?/\\\'\"') for string in out}
            # If startdate and enddate are not specified and the intersection of out and input1 is not empty
            # Add the opinion and title to the output list, add the score to the score list, and update the graph_values
            if startdate == None and enddate == None and (out & input1):
                output.append(i[argument[0]])
                score.append(i[argument[1]])
                if graph_date in graph_values.keys() and graph_date != None:
                    graph_values[graph_date] += 1
                elif graph_date != None:
                    graph_values[graph_date] = 1
            # If startdate and enddate are specified and the review date is within the specified range and the intersection of out and input1 is not empty
            # Add the opinion and title to the output list, add the score to the score list, and update the graph_values
            elif startdate != None and enddate != None and startdate[0] <= review_date[0] <= enddate[0] and startdate[1] <= review_date[1] <= enddate[1] and startdate[2] <= review_date[2] <= enddate[2] and (out & input1):
                output.append(i[argument][0])
                score.append(i[argument[1]])
                if graph_date in graph_values.keys() and graph_date != None:
                    graph_values[graph_date] += 1
                elif graph_date != None:
                    graph_values[graph_date] = 1

        if k == number_of_reviews and number_of_reviews != 0:
            break
        elif k == len(data) and number_of_reviews == 0:
            break
        elif startdate != None and enddate != None and review_date[0] == enddate[0] and review_date[1] == enddate[1] and review_date[2] < enddate[2]:
            break
        k += 1
    # Closing file
    f.close()
    return output, score, k, graph_values