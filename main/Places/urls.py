from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path('home/', TemplateView.as_view(template_name="index.html"), name="home"),
    path("accounts/", include("allauth.urls")),
    path("create/", views.CreatePlaceView.as_view(), name="create"),
    path("place/<slug:pk>/", views.UpdatePlaceView.as_view(), name="update"),
    path("place/<slug:pk>/delete/", views.DeletePlaceView.as_view(), name="delete"),
]
