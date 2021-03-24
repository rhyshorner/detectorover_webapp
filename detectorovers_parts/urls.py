from django.urls import path
from . import views

urlpatterns = [
    path("", views.detectorover_index, name="detectorover_index"),
    path("parts_and_sensor_list/", views.parts_and_sensor_list, name="parts_and_sensor_list"),
    path("parts_filter_by_invensense/", views.parts_filter_by_invensense, name="parts_filter_by_invensense"),
    path("parts_ordered_by_supplier/", views.parts_ordered_by_supplier, name="parts_ordered_by_supplier"),
    path("last_ten_parts/", views.last_ten_parts, name="last_ten_parts"),
]