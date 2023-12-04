from django.shortcuts import render,redirect
from django.views.generic import View,FormView
from django.contrib.auth import authenticate,login,logout

from hr.forms import LoginForm
# Create your views here.

class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm

def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("login sucess")
                return redirect("sign_in")
        