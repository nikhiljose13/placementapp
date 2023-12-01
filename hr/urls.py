from django.urls import path
from hr import views



urlpatterns = [
   path("signin",views.SigninView.as_view(),name="sign_in")
]
