from django.shortcuts import render

from porta.models import Project
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})
