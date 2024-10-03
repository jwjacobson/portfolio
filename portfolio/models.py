from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)