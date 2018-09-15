from django.contrib import admin
from .models import Tool

# Register your models here.
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'order')
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Tool, ToolAdmin)