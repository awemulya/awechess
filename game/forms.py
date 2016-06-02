from django import forms


class SearchGameForm(forms.Form):
    moves = forms.CharField(widget=forms.Textarea)