from django import forms
from .models import Victima

class VictimaForm(forms.ModelForm):

    class Meta():
        model = Victima
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'',
            'content':'',
            'order':'',
        }