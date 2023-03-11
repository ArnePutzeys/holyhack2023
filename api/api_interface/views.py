from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from classification_dutch import get_subjects_nl
from classification import get_subjects
from data_count import count
from rest_framework.decorators import api_view
from rest_framework.response import Response


def process_file(path):
    output = []

    if "reviews_pakket" in path:
        language = "dutch"
        topics = get_subjects_nl(path, language)
    else:
        language = "english"
        topics = get_subjects(path, language)


    print(f"topics: {list(topics.keys())}")
    inputs = list(dict.fromkeys([x.lower() for x in list(topics.keys())]))
    print(inputs)
    result = count(inputs, path, None, None, 2000)
    print(f"result: {result}")

    output = []
    print(result)
    for num in range(0, len(result[0])):
        print(f'gem {result[5]}')
        if language == "dutch":
            output.append({'topics': result[0][num],
                        'hoe_vaak_totaal': result[1][num],
                        'hoe_vaak_procent': result[2][num],
                        'polariteit': result[3][num],
                        'gem_review': result[5][num],
                        'tijdsvoorkomen': result[6],  # add [num]
                        # 'keywords': topics[result[0][num]],
                        })
        else:
            output.append({'topics': result[0][num],
                        'hoe_vaak_totaal': result[1][num],
                        'hoe_vaak_procent': result[2][num],
                        'polariteit': result[3][num],
                        'subjectiviteit': result[4][num],
                        'gem_review': result[5][num],
                        'tijdsvoorkomen': result[6],  # add [num]
                        # 'keywords': topics[result[0][num]],
                        })
    return output




@api_view(('POST',))
def handle_search(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        company = data.get('company', '')
        keywords = data.get('keywords', '')
        start_date = data.get('start_date', '')
        end_date = data.get('end_date', '')

        if 'spotify' in company.lower():
            path = r'C:\Users\kjell\Downloads\holyhack\spotify_data.json'
        else:
            path = r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json'

        result = count(keywords, path, None, None, 2000)
        output = []
        print(result)
        for num in range(0, len(result[0])):
            if not 'spotify' in company.lower():
                output.append({'topics': result[0][num],
                            'start_date': start_date,
                            'end_date': end_date,
                            'hoe_vaak_totaal': result[1][num],
                            'hoe_vaak_procent': result[2][num],
                            'polariteit': result[3][num],
                            'gem_review': result[5][num],
                            'tijdsvoorkomen': result[6],  # add [num]
                            # 'keywords': topics[result[0][num]],
                            })
            else:
                output.append({'topics': result[0][num],
                            'start_date': start_date,
                            'end_date': end_date,
                            'hoe_vaak_totaal': result[1][num],
                            'hoe_vaak_procent': result[2][num],
                            'polariteit': result[3][num],
                            'subjectiviteit': result[4][num],
                            'gem_review': result[5][num],
                            'tijdsvoorkomen': result[6],  # add [num]
                            # 'keywords': topics[result[0][num]],
                            })
        print(output)
        return Response(output)
    else:
        return Response({'result': 'error', 'message': 'Invalid request method, POST required'})


@api_view(['GET', 'OPTIONS'])
def get_search_result(request):
    return Response(process_file(r'C:\Users\kjell\Downloads\holyhack\spotify_data.json'))
    #return Response([process_file(r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json'), process_file(r'C:\Users\kjell\Downloads\holyhack\spotify_data.json')])

# @api_view(['GET', 'OPTIONS'])
# def get_search_result(request):
#     if request.method == 'GET':
#         # format: {subject1: [keyw1, keyw2, ...], subject2: [...], ...}
#         pakket_topics = get_subjects_nl(r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json', 'dutch')
#         # spotify_topics = get_subjects(r'C:\Users\kjell\Downloads\holyhack\spotify_data.json', 'english')

#         # expected output: {(keywords), hoe_vaak_totaal, hoe_vaak_procent, polariteit, (subjectiviteit), gem_review, tijdsvoorkomen}
#         # Only analyzing the subject for now
#         # output count: keywords,totaal,procent,polariteit,sentiment,gem_review,tijdsvoorkomen
#         # nog een probleem: soms is de topic 'the topic is: ...' ipv gewoon 'topic'

#         print(f"pakket_topics: {list(pakket_topics.keys())}")
#         inputs = list(dict.fromkeys([x.lower()
#                     for x in list(pakket_topics.keys())]))
#         print(inputs)
#         pakket_result = count(inputs, r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json', None, None, 2000)
#         print(f"pakket_result: {pakket_result}")
#         # pakket_result = [['kaas'], ['500'], ['20'], ['0.97'], ['0.5'], ['3.7'], ['']]
#         # spotify_result = count(list(spotify_topics.keys()))

#         output = []
#         print(pakket_result)
#         for num in range(0, len(pakket_result[0])):
#             print(f'gem {pakket_result[5]}')
#             output.append({'topics': pakket_result[0][num],
#                         'hoe_vaak_totaal': pakket_result[1][num],
#                         'hoe_vaak_procent': pakket_result[2][num],
#                         'polariteit': pakket_result[3][num],
#                         'gem_review': pakket_result[5][num],
#                         'tijdsvoorkomen': pakket_result[6],  # add [num]
#                         # 'keywords': pakket_topics[pakket_result[0][num]],
#                         })

#         return Response(output)
#     elif request.method == 'OPTIONS':
#         # Handle OPTIONS request here
#         response = Response()
#         response['Access-Control-Allow-Origin'] = '*'
#         response['Access-Control-Allow-Methods'] = 'GET'
#         response['Access-Control-Allow-Headers'] = 'Content-Type'
#         return response

@api_view(['GET'])
def get_competition(request):
    # Example with Deezer reviews
    output = []

    # format: {subject1: [keyw1, keyw2, ...], subject2: [...], ...}
    # pakket_topics = get_subjects_nl(r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json', 'dutch')
    spotify_topics = get_subjects(r'C:\Users\kjell\Downloads\holyhack\spotify_data.json', 'english')

    print(f"spotify_topics: {list(spotify_topics.keys())}")
    inputs = list(dict.fromkeys([x.lower()
                  for x in list(spotify_topics.keys())]))
    print(inputs)
    spotify_result = count(inputs, r'C:\Users\kjell\Downloads\holyhack\outputkevkevformat.json', None, None, 2000)
    print(f"pakket_result: {spotify_result}")

    output = []
    print(spotify_result)
    for num in range(0, len(spotify_result[0])):
        print(f'gem {spotify_result[5]}')
        output.append({'topics': spotify_result[0][num],
                       'hoe_vaak_totaal': spotify_result[1][num],
                       'hoe_vaak_procent': spotify_result[2][num],
                       'polariteit': spotify_result[3][num],
                       'gem_review': spotify_result[5][num],
                       'tijdsvoorkomen': spotify_result[6],  # add [num]
                       # 'keywords': pakket_topics[pakket_result[0][num]],
                       })

    return Response(output)
