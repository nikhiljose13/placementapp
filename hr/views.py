from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from myapp.models import Category,Jobs
from hr.forms import LoginForm,CategoryForm,JobForm
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
     
class CategoryListcreateView(CreateView,ListView):
     template_name="category.html"
     form_class=CategoryForm
     success_url=reverse_lazy("category")
     context_object_name="data"
     model=Category

class CategoryDeletecreateView(View):

      def get(self,request,*args,**kwargs):
           id=kwargs.get("pk")
           Category.objects.filter(id=id).delete()
           return redirect("category")
      
class JobCreateView(CreateView):

     template_name="job_add.html"
     form_class=JobForm
     success_url=reverse_lazy("index")

class JobListView(ListView):

     template_name="job_list.html"
     context_object_name="jobs"
     model=Jobs

class JobDeleteView(View):
     def get(self,request,*args,**kwargs):
          id=kwargs.get("pk")
          Jobs.objects.filter(id=id).delete()
          return redirect("index")