from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Victima
from .forms import VictimaForm

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class VictimaListView(ListView):
    model = Victima

class VictimaDetailView(DetailView):
    model = Victima

@method_decorator(staff_member_required, name='dispatch')
class VictimaCreate(CreateView):
    model = Victima
    form_class = VictimaForm
    success_url = reverse_lazy('victimas:victimas')

@method_decorator(staff_member_required, name='dispatch')
class VictimaUpdate(UpdateView):
    model = Victima
    form_class = VictimaForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('victimas:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class VictimaDelete(DeleteView):
    model = Victima
    success_url = reverse_lazy('victimas:victimas')