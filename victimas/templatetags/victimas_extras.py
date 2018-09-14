from django import template
from victimas.models import Victima

register = template.Library()

@register.simple_tag
def get_victima_list():
    victimas = Victima.objects.all()
    return victimas