from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    pakket_topics = get_subjects(r'C:\Users\kjell\Downloads\holyhack\reviews_pakket.json', 'dutch')
    spotify_topics = get_subjects(r'C:\Users\kjell\Downloads\holyhack\spotify_data.json', 'english')

    #expected output: {(keywords), hoe_vaak_totaal, hoe_vaak_procent, polariteit, (subjectiviteit), gem_review, tijdsvoorkomen}
    data = []
    # Only analyzing the subject for now
    for topic in pakket_topics.keys():
        data.append(count(topic))
        
    for topic in spotify_topics.keys():
        data.append(count(topic))
    
    return Response(data)
