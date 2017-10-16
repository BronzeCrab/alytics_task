from django import forms


class TestForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
