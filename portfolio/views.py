# portfolio -- Jeff Jacobson's personal portfolio
# Copyright (C) 2024 Jeff Jacobson <jeffjacobsonhimself@gmail.com>
#       
#   
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
    
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
        
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from django.conf import settings
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

def about(request):
    return render(request, "portfolio/_about.html",
        {"MEDIA_URL": settings.MEDIA_URL} 
        )