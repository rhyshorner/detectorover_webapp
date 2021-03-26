from django.shortcuts import render
from detectorovers_parts.models import Part

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

