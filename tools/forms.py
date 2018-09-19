from django import forms
from .models import Tool

class ToolForm(forms.ModelForm):

    class Meta():
        model = Tool
        fields = ['name', 'imagen', 'content', 'link', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'imagen': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Link a la herramienta'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'name':'',
            'imagen':'',
            'content':'',
            'link':'',
            'order':'',
        }