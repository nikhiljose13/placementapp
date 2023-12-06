from django import forms 
from myapp.models import Category


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    
class  CategoryForm(forms.ModelForm):

    class Meta:
        model=Category
        fields=["name"]