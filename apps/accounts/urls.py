from django.urls import path
from apps.accounts.views import UserProfileView, UserCreateView, UserLoginView

# from .views import UserProfileView

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]
