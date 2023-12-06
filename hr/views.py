from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

from hr.forms import LoginForm,CategoryForm
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
                    return redirect("index")
            print("invalid")
            return render(request,"login.html",{"form":form})
    
class DashBoardView(TemplateView):
     template_name="index.html"


class signOutView(View):
     def get(self,request,*args,**kwargs):
          logout(request)
          return redirect("sign_in")
     
class CategoryListcreateView(CreateView):
     template_name="category.html"
     form_class=CategoryForm
     success_url=reverse_lazy("category")