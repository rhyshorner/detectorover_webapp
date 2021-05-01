from django.urls import path
from . import views

urlpatterns = [
    path("weather_page/", views.weather_app_index, name="weather_app_index"),
    path("weather_page/sydney_weather_page", views.sydney_weather_page, name="sydney_weather_page"),
    path("weather_api/", views.weather_api, name="weather_api")]