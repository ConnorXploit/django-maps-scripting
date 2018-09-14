from django.contrib import admin
from .models import Victima

# Register your models here.
class VictimaAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Victima, VictimaAdmin)