from django.shortcuts import render
from django.views.generic import View

from hr.forms import Loginform
# Create your views here.

class SigninView(View):
    def get(self,reuest,*args,**kwargs):
        form=Loginform()
        return render(reuest,"signin.html",{"form":form})