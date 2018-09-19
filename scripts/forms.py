from django import forms
from .models import Script

class ScriptForm(forms.ModelForm):
    class Meta():
        model = Script
        fields = ['name', 'imagen', 'content', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'imagen': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'name':'',
            'imagen':'',
            'content':'',
            'order':'',
        }