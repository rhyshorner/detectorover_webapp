from django.shortcuts import render
from detectorovers_parts.models import Part

# Create your views here.

def detectorover_index(request):
    return render(request, 'detectorover_index.html')

def parts_and_sensor_list(request):
    parts = Part.objects.all()
    context = {
        'parts':parts
    }
    return render(request, 'parts_and_sensor_list.html', context)

def parts_by_single_supplier(request):
    parts = Part.objects.get(supplier__iexact="InvenSense")
    context = {'parts':parts}
    return render(request, 'parts_by_single_supplier.html', context)

def parts_ordered_by_supplier(request):
    parts = Part.objects.order_by('headline')[0]
    context = {'parts':parts}
    return render(request, 'parts_ordered_by_supplier.html', context)

def last_ten_parts(request):
    last_ten = Part.objects.filter(since=since).order_by('-id')[:10]
    context = reversed(last_ten)
    return render(request, 'last_ten_parts.html', context)

