from django.urls import path

from jobseeker import views


urlpatterns = [
   path("register/",views.SignUpView.as_view(),name="signup"),
   path("index/",views.StudentIndexView.as_view(),name="seeker-index"),
   path("profiles/add",views.ProfileCreateView.as_view(),name="profile-add"),
   path("profiles/<int:pk>/",views.ProfileDetailView.as_view(),name="profile-detail"),
   path("profiles/<int:pk>/change",views.ProfileEditView.as_view(),name="profile-edit"),
]
