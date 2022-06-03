from django import forms
from example.models import Author

class NewsAddForm(forms.Form):
    # This is a simple form
    title = forms.CharField(max_length=30)
    # This is how to create a text box
    body = forms.CharField(widget=forms.Textarea)
    # This is a dropdown choice field from a model
    author = forms.ModelChoiceField(queryset=Author.objects.all())