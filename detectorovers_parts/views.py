from django.shortcuts import render
from detectorovers_parts.models import Part

# Create your views here.

def detectorover_index(request):
    parts = Part.objects.all()
    context = {
        'parts':parts
    }
    return render(request, 'detectorover_index.html', context)

def parts_and_sensor_list(request):
    parts = Part.objects.all()
    context = {
        'parts':parts
    }
    return render(request, 'parts_and_sensor_list.html', context)

