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
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    def published(self):
        return self.filter(
            published_at__isnull=False,
            published_at__lte=timezone.now(),
        )


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    original_url = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    image_alt = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        ordering = ['-published_at']

    @property
    def is_published(self):
        return self.published_at is not None and self.published_at <= timezone.now()

    def __str__(self):
        if self.is_published:
            return self.title
        return f"{self.title} (draft)"
