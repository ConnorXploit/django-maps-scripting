from django.urls import path
from .views import ToolCreate, ToolUpdate, ToolDelete, ToolListView, ToolDetailView

tools_patterns = ([
    path('', ToolListView.as_view(), name='tools'),
    path('<int:pk>/<slug:slug>/', ToolDetailView.as_view(), name='tool'),
    path('create/', ToolCreate.as_view(), name='create'),
    path('update/<int:pk>', ToolUpdate.as_view(), name='update'),
    path('delete/<int:pk>', ToolDelete.as_view(), name='delete'),
], 'tools')