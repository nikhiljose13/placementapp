from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView
from myapp.models import  StudentProfile,Jobs,Applications
from jobseeker.forms import RegistrationForm,ProfileForm
# Create your views here.

class SignUpView(CreateView):

    template_name="jobseeker/register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("sign_in")

class StudentIndexView(ListView):
    template_name="jobseeker/index.html"
    context_object_name="data"
    model=Jobs
    def get_queryset(self) :
         qs=Jobs.objects.all().order_by("-Created_date")
         return qs

class ProfileCreateView(CreateView):

        template_name="jobseeker/register.html"
        form_class=ProfileForm
        success_url=reverse_lazy("seeker-index")

        def form_valid(self, form):
             form.instance.user=self.request.user
             return super().form_valid(form)

class ProfileDetailView(DetailView):
     
     template_name="jobseeker/profile_detail.html"
     context_object_name="data"
     model=StudentProfile

class ProfileEditView(UpdateView):
     template_name="jobseeker/profile_edit.html"
     form_class=ProfileForm
     model=StudentProfile
     success_url=reverse_lazy("seeker-index")


class JobDetailView(DetailView):
     template_name="jobseeker/job_detail.html"
     model=Jobs
     context_object_name="data"

class ApplyJobView(View):
   def post(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       job_obj=Jobs.objects.get(id=id)
       student_obj = request.user
       Applications.objects.create(job=job_obj, student=student_obj)
       return redirect("seeker-index")