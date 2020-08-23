from django import forms
from .models import Category

class CategoryForm (forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= Category
        fields=['title']