from django.urls import path
from .views import handle_search, get_search_result

urlpatterns = [
    path('search/', handle_search, name='handle_search'),
    path('topics/', get_search_result, name='get_search_result')
]
