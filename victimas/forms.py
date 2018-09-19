from django import forms
from .models import Victima

class VictimaForm(forms.ModelForm):

    class Meta():
        model = Victima
        fields = ['title', 'imagen', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'imagen': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'',
            'imagen':'',
            'content':'',
            'order':'',
        }