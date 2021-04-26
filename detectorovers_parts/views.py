from django.shortcuts import render
from detectorovers_parts.models import Part
import requests as req
import os

# Create your views here.

def detectorover_index(request):
    return render(request, 'detectorover_index.html')

def parts_and_sensor_list(request):
    parts = Part.objects.all()
    context = {'parts':parts}
    return render(request, 'parts_and_sensor_list.html', context)

def parts_filter_by_invensense(request):
    parts = Part.objects.filter(manufacturer__contains='InvenSense')
    context = {'parts':parts}
    return render(request, 'parts_filter_by_invensense.html', context)

def parts_ordered_by_supplier(request):
    parts = Part.objects.order_by('supplier')
    context = {'parts':parts}
    return render(request, 'parts_ordered_by_supplier.html', context)

def last_ten_parts(request):
    parts = Part.objects.order_by('-id')[:10]
    context = {'parts':parts}
    return render(request, 'last_ten_parts.html', context)

def weather_page(request):
    owmapi_key =  os.environ['OWM_KEY']
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {
        'q': 'Sydney,AU',
        'appid': owmapi_key,
        'units':'metric'
    }
    resp = req.get(base_url, params=parameters)
    resp = resp.json()
    context = {'resp':resp}
    return render(request, 'weather_page.html', context)