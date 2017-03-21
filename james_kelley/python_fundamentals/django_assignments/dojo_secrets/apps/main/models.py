from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def validate_user(self, post):
		isValid = True
		if not EMAIL_REGEX.match(post.get('email')):
			isValid = False
		if len(post.get('first_name')) == 0:
			isValid = False
		if len(post.get('last_name')) == 0:
			isValid = False
		if len(post.get('email')) == 0:
			isValid = False
		if len(post.get('pass')) < 8:
			isValid = False
		if post.get('pass') != post.get('pass_conf'):
			isValid = False
		return isValid

	def login_user(self, post):
		user = self.filter(email=post.get('email')).first()
		if user and bcrypt.hashpw(post.get('pass').encode(), user.password.encode()) == user.password:
			return(True, user)
		else:
			return(False)


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Secret(models.Model):
	secret = models.TextField()
	creator = models.ForeignKey(User, related_name='secrets')
	likes = models.ManyToManyField(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

