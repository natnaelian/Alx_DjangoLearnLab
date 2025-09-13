# bookshelf/forms.py
from django import forms

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=50, required=True)