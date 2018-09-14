from django.conf.urls import url                                                                                                                              
from . import views

urlpatterns = [ 
    url('', views.default_map, name="default"),
]