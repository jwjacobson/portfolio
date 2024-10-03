from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    blurb = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="Description goes here")
    core_tech = models.CharField(max_length=200, null=True, blank=True)
    supporting_tech = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} | {self.blurb}"