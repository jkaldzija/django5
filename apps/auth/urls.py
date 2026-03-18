from django.urls import path

from apps.auth.views import LoginView, RefreshAccessTokenView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshAccessTokenView.as_view(), name="token_refresh"),
]
