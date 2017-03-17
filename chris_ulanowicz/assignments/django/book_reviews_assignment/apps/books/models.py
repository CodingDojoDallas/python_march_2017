from __future__ import unicode_literals

from django.db import models
from ..authors.models import Author

class Book(models.Model):
	title = models.CharField(max_length=255, unique=True)
	author = models.ForeignKey(Author, related_name='authored_books')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)