from django.contrib import admin
from .models import Script

# Register your models here.
class ScriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'imagen', 'order')
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Script, ScriptAdmin)