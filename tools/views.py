from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Tool
from .forms import ToolForm

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ToolListView(ListView):
    model = Tool

class ToolDetailView(DetailView):
    model = Tool

@method_decorator(staff_member_required, name='dispatch')
class ToolCreate(CreateView):
    model = Tool
    form_class = ToolForm
    success_url = reverse_lazy('tools:tools')

@method_decorator(staff_member_required, name='dispatch')
class ToolUpdate(UpdateView):
    model = Tool
    form_class = ToolForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('tools:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ToolDelete(DeleteView):
    model = Tool
    success_url = reverse_lazy('tools:tools')