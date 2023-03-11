from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
                     'hoe_vaak_procent'
                     'polariteit': '0 of 1',
                     'subjectiviteit': '-1 of 1',
                     'gem_review': '...',
                     'tijdsvoorkomen': '...',
            }
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'result': 'error', 'message': 'Invalid request method, POST required'})
    


#@api_view(['GET'])
#def get_search_result(request):
#    my_data = {
#        'hoe_vaak_totaal': '...',
#        'polariteit': '0 of 1',
#        'subjectiviteit': '-1 of 1',
#        'gem_review': '...',
#        'tijdsvoorkomen': '...',
#    }
#    
#    return Response(my_data)
