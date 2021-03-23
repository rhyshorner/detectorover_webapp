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

# need to fix this
def part_supplier(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

