from django import forms
from .models import Tool

class ToolForm(forms.ModelForm):

    class Meta():
        model = Tool
        fields = ['name', 'content', 'link', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'name':'',
            'content':'',
            'link':'',
            'order':'',
        }