from django.urls import path
from .views import handle_search

urlpatterns = [
    path('search/', handle_search, name='handle_search'),
]
