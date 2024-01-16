# forms.py
from django import forms


class SampleForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(min_length=3)
    favourite_color = forms.CharField()
