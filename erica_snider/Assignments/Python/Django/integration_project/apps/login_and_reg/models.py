from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models

import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# password = "super secret password"


class UserManager(models.Manager):

    def register(self, postData):
        errors = []
        # VALIDATE FIRST NAME
        if len(postData['first_name']) < 1:
            errors.append('First name cannot be empty.')
        elif len(postData['first_name']) <= 2:
            errors.append('First name must be at least two characters.')
        # VALIDATE LAST NAME
        if len(postData['last_name']) < 1:
            errors.append('Last name cannot be empty.')
        elif len(postData['last_name']) <= 2:
            errors.append('Last name must be at least two characters.')
        # VALIDATE EMAIL
        if len(postData['email']) < 1:
            errors.append('Email cannot be empty')
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append("Email address must be valid.")
        else:
            try:
                user = User.objects.get(email=postData['email'])
            except MultipleObjectsReturned:
                errors.append("Email address has already been registered.")
            except:
                pass
        # VALIDATE PASSWORD
        if len(postData['password']) < 1:
            errors.append("Password cannot be empty.")
        elif len(postData['password']) < 8:
            errors.append("Password must be at least 8 characters.")
        # VALIDATE PASSWORD CONFIRMATION
        if postData['password'] != postData['password_conf']:
            errors.append("Passwords must match.")

        if len(errors) > 0:
            return (False, errors)
        else:
            #ORM query to create
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()) # creates hashed password to be saved in db
            new_user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed)
            # new_user.save()
            print 'the new user is', new_user
            return (True, new_user.first_name)


    def login(self, postData):
        errors = []
        # VALIDATE EMAIL
        if len(postData['email']) < 1:
            errors.append('Email cannot be empty')
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append("Email address must be valid.")
        # VALIDATE PASSWORD
        if len(postData['password']) < 1:
            errors.append("Password cannot be empty.")
        elif len(postData['password']) < 8:
            errors.append("Password must be at least 8 characters.")

        if len(errors) > 0:
            return (False, errors)
        else:
            try:
                user = User.objects.get(email=postData['email'])
            except ObjectDoesNotExist:
                errors.append("Email or password is invalid. (email not found)")
                return (False, errors)
            except MultipleObjectsReturned:
                errors.append("Email or password is invalid. (more than one entry with that email)")
                return (False, errors)
            if user.password == bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
                return (True, user.first_name)
            else:
                errors.append("Email or password is invalid. (password doesn't match)")
                return (False, errors)


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
