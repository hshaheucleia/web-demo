
from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', required=False, widget=forms.TextInput(attrs={'class':'typeahead', 'placeholder': "By Institute name/city/pin"}))