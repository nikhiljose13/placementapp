from django.urls import path

from jobseeker import views


urlpatterns = [
   path("register/",views.SignUpView.as_view(),name="signup"),
   path("index/",views.StudentIndexView.as_view(),name="seeker_index"),
]
