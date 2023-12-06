from django.urls import path
from hr import views



urlpatterns = [
   path("signin",views.SigninView.as_view(),name="sign_in"),
   path("index",views.DashBoardView.as_view(),name="index"),
   path("signout",views.signOutView.as_view(),name="signout"),
   path("category",views.CategoryListcreateView.as_view(),name="category"),
   path("category/<int:pk>/remove/",views.CategoryDeletecreateView.as_view(),name="category-delete")
]
