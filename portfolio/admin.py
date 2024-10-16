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

from django.contrib import admin

from portfolio.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "blurb", "url"]
    search_fields = ("title",)