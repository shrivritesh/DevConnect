from django.urls import path
from .views import RegisterView, LoginView, ProfileView ,UpdateProfileView,ChangePasswordView,LogoutView 

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("me/", ProfileView.as_view(), name="profile"),
    path("me/update/", UpdateProfileView.as_view()),
    path("change-password/",ChangePasswordView.as_view(),name="change-password"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
