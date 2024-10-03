from django.shortcuts import render

from portfolio.models import Project

def index(request):
    projects = Project.objects.all()

    return render(
        request, "portfolio/index.html",
        {"projects": projects}
        )