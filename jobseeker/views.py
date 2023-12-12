from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView

from jobseeker.forms import RegistrationForm
# Create your views here.

class SignUpView(CreateView):

    template_name="jobseeker/register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("sign_in")

class StudentIndexView(TemplateView):
    template_name="jobseeker/index.html"

