from django import forms

class TwitterForm(forms.Form):
    text = forms.CharField(label="tweet", max_length=140)
