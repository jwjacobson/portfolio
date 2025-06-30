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

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    blurb = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="Description goes here")
    core_tech = models.CharField(max_length=200, null=True, blank=True)
    supporting_tech = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    screenshot = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.title} | {self.blurb}"