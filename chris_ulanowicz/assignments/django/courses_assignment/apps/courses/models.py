from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=45)
	description = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
