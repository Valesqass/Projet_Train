from django import forms

class Recherche(forms.Form):
    query = forms.CharField(label="Votre recherche", max_length=100)
