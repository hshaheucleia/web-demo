
from django import forms


class SearchForm(forms.Form):
    univ_name = forms.CharField(max_length=100, required=False)
    univ_state = forms.CharField(max_length=50, required=False)
    univ_pin = forms.CharField(max_length=6, required=False)