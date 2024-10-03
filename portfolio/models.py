from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    blurb = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)