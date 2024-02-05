from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls"), namespace="blog"),
    path("api/", include("api.urls"), namespace="blog_api"),
]
