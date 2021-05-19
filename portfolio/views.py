from django.shortcuts import render

# Create your views here.
from portfolio.models import Project

def portfolio_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)