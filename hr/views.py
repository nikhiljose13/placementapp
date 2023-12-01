from django.shortcuts import render
from django.views.generic import View,FormView

from hr.forms import Loginform
# Create your views here.

class SigninView(FormView):
    template_name="login.html"
    form_class=Loginform