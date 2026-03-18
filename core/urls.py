from django.contrib import admin
from django.urls import include, path

from core.views import ping

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/ping/", ping, name="ping"),
    path("api/auth/", include("apps.auth.urls")),
    path("api/users/", include("apps.users.urls")),
]
