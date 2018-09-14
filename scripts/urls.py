from django.urls import path
from .views import ScriptCreate, ScriptDelete, ScriptUpdate, ScriptDetailView, ScriptListView

scripts_patterns = ([
    path('', ScriptListView.as_view(), name='scripts'),
    path('<int:pk>/<slug:slug>/', ScriptDetailView.as_view(), name='script'),
    path('create/', ScriptCreate.as_view(), name='create'),
    path('update/<int:pk>', ScriptUpdate.as_view(), name='update'),
    path('delete/<int:pk>', ScriptDelete.as_view(), name='delete'),
], 'scripts')