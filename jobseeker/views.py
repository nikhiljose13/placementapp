from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView
from myapp.models import  StudentProfile
from jobseeker.forms import RegistrationForm,ProfileForm
# Create your views here.

class SignUpView(CreateView):

    template_name="jobseeker/register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("sign_in")

class StudentIndexView(TemplateView):
    template_name="jobseeker/index.html"



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



