from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=120, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
