from django.shortcuts import render

from portfolio.models import Project

def index(request):
    projects = Project.objects.all()

    if request.headers.get('HX-Request'):  
        return render(request, 'portfolio/_projects.html', {'projects': projects})

    return render(
        request, "portfolio/index.html",
        {"projects": projects}
        )

def details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(
        request, "portfolio/_details.html",
        {"project": project}
        )
