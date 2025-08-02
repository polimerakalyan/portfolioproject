from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'home.html')



def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})

def contact(request):
    return render(request, 'contact.html')

def hireme(request):
    return render(request,'hire.html')
