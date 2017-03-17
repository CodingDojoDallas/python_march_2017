from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User

class Course(models.Model):
	creator = models.ForeignKey(User, related_name='courses_created')
	name = models.CharField(max_length=45)
	description = models.TextField(null=True)
	students = models.ManyToManyField(User, related_name='courses_joined')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
