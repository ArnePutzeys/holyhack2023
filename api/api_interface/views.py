from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, sys, os
from rest_framework.decorators import api_view
from rest_framework.response import Response
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_count import count
from classification import get_subjects

@csrf_exempt
def handle_search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        company = data.get('company', '')
        keywords = data.get('keywords', '')

        # do some processing based on the keywords
        ...

        response_data = {
            'result': 'success',
            'data': {'hoe_vaak_totaal': '...',
                     'diagram_type': '...',
                     'hoe_vaak_procent': '...',
                     'polariteit': '0 of 1',
                     'subjectiviteit': '-1 of 1',
                     'gem_review': '...',
                     'tijdsvoorkomen': '...',
            }
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'result': 'error', 'message': 'Invalid request method, POST required'})


@api_view(['GET'])
def get_search_result(request):
    #format: {subject1: [keyw1, keyw2, ...], subject2: [...], ...}
    #pakket_topics = get_subjects(r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json', 'dutch')
    #spotify_topics = get_subjects(r'C:\Users\kjell\Downloads\holyhack\spotify_data.json', 'english')
    print('got here m8')
    #expected output: {(keywords), hoe_vaak_totaal, hoe_vaak_procent, polariteit, (subjectiviteit), gem_review, tijdsvoorkomen}
    # Only analyzing the subject for now
    # output count: keywords,totaal,procent,polariteit,sentiment,gem_review,tijdsvoorkomen
    #nog een probleem: soms is de topic 'the topic is: ...' ipv gewoon 'topic'
    #pakket_result = count(list(pakket_topics.keys()[0]), r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json')
    pakket_result = [['kaas'], ['500'], ['20'], ['0.97'], ['0.5'], ['3.7'], ['']]
    #spotify_result = count(list(spotify_topics.keys()))

    print('nice we got here')
    output = []
    for num in range(0, len(pakket_result[0])):
        print(len(pakket_result) - 1)
        print(pakket_result[0], num)
        output.append({'topics': pakket_result[0][num],
                        'hoe_vaak_totaal': pakket_result[1][num],
                        'hoe_vaak_procent': pakket_result[2][num],
                        'polariteit': pakket_result[3][num],
                        'gem_review': pakket_result[5][num],
                        'tijdsvoorkomen': pakket_result[6][num],
                        #'keywords': pakket_topics[pakket_result[0][num]],
                        })

    return Response(output)
