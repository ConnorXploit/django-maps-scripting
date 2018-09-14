from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Script
from .forms import ScriptForm

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ScriptListView(ListView):
    model = Script

class ScriptDetailView(DetailView):
    model = Script

@method_decorator(staff_member_required, name='dispatch')
class ScriptCreate(CreateView):
    model = Script
    form_class = ScriptForm
    success_url = reverse_lazy('scripts:scripts')

@method_decorator(staff_member_required, name='dispatch')
class ScriptUpdate(UpdateView):
    model = Script
    form_class = ScriptForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('scripts:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ScriptDelete(DeleteView):
    model = Script
    success_url = reverse_lazy('scripts:scripts')