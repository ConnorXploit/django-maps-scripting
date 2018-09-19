from django.urls import path                                                                                                                              
from .views import HomeListView

inicio_patterns = ([
    path('', HomeListView.as_view(), name='inicio'),
], 'inicio')