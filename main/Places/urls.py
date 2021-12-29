from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.ListPlaceView.as_view(), name="home"),
    path('home/', views.ListPlaceView.as_view(), name="home"),
    path("accounts/", include("allauth.urls")),
    path("create/", views.CreatePlaceView.as_view(), name="create"),
    path("place/<slug:pk>/", views.UpdatePlaceView.as_view(), name="update"),
    path("place/<slug:pk>/delete/", views.DeletePlaceView.as_view(), name="delete"),
]
