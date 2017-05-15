from __future__ import unicode_literals

from django.db import models

import re # the "re" module will let us perform some regular expression operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def login(self, postData):
        print "Running a login function!"
        print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
        print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
        pass
    def register(self, postData):
        print ("Register a user here")
        print ("If successful, maybe return {'theuser':user} where user is a user object?")
        print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
        pass
    def validate(self, postData):
        # print ("Validate the user-supplied email address here")
        # print ("If successful, maybe return {'theuser':user} where user is a user object?")
        # print ("If unsuccessful do something like this? return {'errors':['Email not valid']}")
        if len(postData) < 1:
            validation = {'errors':['Email cannot be empty']}
        elif not EMAIL_REGEX.match(postData):
            validation = {'errors':['Email not valid']}
        else:
            validation = {'success':[postData]}
            # on successful validation, insert email into database and redirect to success page
        return validation

class Email(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************
