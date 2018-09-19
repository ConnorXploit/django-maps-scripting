from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from .models import Home
from victimas.models import Victima
from scripts.models import Script
from tools.models import Tool

# Create your views here.

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class HomeListView(ListView):
    model = Home

    def get_context_data(self, *args, **kwargs):
        context = super(HomeListView, self).get_context_data(*args, **kwargs)
        context['victimas_list'] = Victima.objects.all()
        context['tools_list'] = Tool.objects.all()
        context['scripts_list'] = Script.objects.all()
        return context