from django.urls import path

app_name = "api"

from . import views

urlpatterns = [path("", views.HomeView.as_view(), name="home")]
