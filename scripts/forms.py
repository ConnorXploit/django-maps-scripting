from django import forms
from .models import Script

class ScriptForm(forms.ModelForm):

    class Meta():
        model = Script
        fields = ['name', 'content', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'name':'',
            'content':'',
            'order':'',
        }