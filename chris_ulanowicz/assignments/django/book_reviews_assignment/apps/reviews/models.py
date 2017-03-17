from __future__ import unicode_literals

from django.db import models
from ..books.models import Book
from ..login_registration.models import User

class Review(models.Model):
	content = models.TextField()
	rating = models.PositiveSmallIntegerField()
	book = models.ForeignKey(Book, related_name='reviews')
	reviewer = models.ForeignKey(User, related_name='book_reviews')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)