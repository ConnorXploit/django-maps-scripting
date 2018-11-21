from django.urls import path
from .views import VictimaListView, VictimaDetailView, VictimaCreate, VictimaUpdate, VictimaDelete

victimas_patterns = ([
    path('', VictimaListView.as_view(), name='objetivos'),
    path('<int:pk>/<slug:slug>/', VictimaDetailView.as_view(), name='objetivo'),
    path('create/', VictimaCreate.as_view(), name='create'),
    path('update/<int:pk>', VictimaUpdate.as_view(), name='update'),
    path('delete/<int:pk>', VictimaDelete.as_view(), name='delete'),
], 'objetivos')