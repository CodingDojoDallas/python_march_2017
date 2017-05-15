from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Message(models.Model):
    creator = models.ForeignKey(User, related_name='users_message')
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    creator = models.ForeignKey(User, related_name='users_comment')
    on_message = models.ForeignKey(Message, related_name='messages_comment')
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

#############
# SOLUTION: #
#############
# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     password = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# class Message(models.Model):
#     message = models.TextField()
#     user = models.ForeignKey(User)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# class Comment(models.Model):
#     comment = models.TextField()
#     user = models.ForeignKey(User)
#     message = models.ForeignKey(Message)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
