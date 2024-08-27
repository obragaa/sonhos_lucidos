
from django import forms
from .models import Sonho

class SonhoForm(forms.ModelForm):
    class Meta:
        model = Sonho
        fields = ['titulo', 'descricao', 'emocao', 'tema', 'nivel_lucidez', 'data', 'duracao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'data': forms.SelectDateWidget(),
        }
