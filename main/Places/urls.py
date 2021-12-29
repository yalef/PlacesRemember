from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("accounts/", include("allauth.urls")),
    path("create/", views.CreatePlaceView.as_view(), name="create"),
]
