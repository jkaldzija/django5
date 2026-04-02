from django.urls import path

from apps.users.api.views import MeView

urlpatterns = [
    path("me/", MeView.as_view(), name="users-me"),
]

