from django.urls import path
from . import views

urlpatterns = [
    path("", views.detectorover_index, name="detectorover_index"),
    path("parts_and_sensor_list/", views.parts_and_sensor_list, name="parts_and_sensor_list"),
]