from django.urls import path
from . import views

urlpatterns = [
    path("", views.detectorover_index, name="detectorover_index"),
    path("parts_and_sensor_list/", views.parts_and_sensor_list, name="parts_and_sensor_list"),
    path("parts_by_single_supplier/", views.parts_by_single_supplier, name="parts_by_single_supplier"),
    path("parts_ordered_by_supplier/", views.parts_ordered_by_supplier, name="parts_ordered_by_supplier"),
    path("last_ten_parts/", views.last_ten_parts, name="last_ten_parts"),
]