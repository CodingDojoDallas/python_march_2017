from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models
from django.db.models import Count
from django.db import connection

import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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
            print 'the newly registered user is', new_user
            return (True, new_user.id, new_user.first_name) # new_user.first_name

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
                if user.password == bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
                    print 'logging in user is ', user
                    return (True, user.id, user.first_name) # user.first_name
                else:
                    errors.append("Email or password is invalid. (password doesn't match)")
                    return (False, errors)
            except ObjectDoesNotExist:
                errors.append("Email or password is invalid. (email not found)")
                return (False, errors)
            except MultipleObjectsReturned:
                errors.append("Email or password is invalid. (more than one entry with that email)")
                return (False, errors)

    def get_likes(self, postData):
        # get an array of ids
        this_user = User.objects.get(id=postData.session['id'])
        # this_users_likes = this_user.all()
        # print "the user id is", postData.session['id']
        # print "this user is" , this_user
        # print "this_users_likes is" , this_user.likes.all()
        this_users_likes = this_user.liked_secrets.all().values_list('id', flat=True)
        # this_secret = Secret.objects.filter(creator_id = postData.session['id'])
        # print [secret.id for secret in this_secret]
        print 'this user is ', this_user
        print 'this users likes is ', this_users_likes
        # likes_on_a_secret = this_secret.likes.all()
        # print 'likes on a secret is ', likes_on_a_secret
        return (True, this_users_likes)

class SecretManager(models.Manager):
    def secrets_recent(self, postData):
        # secrets = Secret.objects.annotate(Count('likes')).order_by('-created_at')[:10]
        # print Secret.objects.annotate(Count('likes')).order_by('-created_at')[:10].query
        secrets = Secret.objects.order_by('-created_at').annotate(Count('likes'))[:10]
        return (True, secrets)

    def secrets_popular(self):
        secrets = Secret.objects.annotate(Count('likes')).order_by('-likes__count')[:10]
        return (True, secrets)

    def create_secret(self, postData):
        errors=[]
        if len(postData.POST['secret']) < 1:
            errors.append('Secret cannot be empty.')
            return (False, errors)
        new_secret_creator = User.objects.get(id=postData.session['id'])
        secret = Secret.objects.create(secret=postData.POST['secret'], creator=new_secret_creator)
        return (True, secret)

    def create_like(self, postData, secret_id):
        this_secret = Secret.objects.get(id=secret_id)
        this_user = User.objects.get(id=postData.session['id'])
        this_secret.likes.add(this_user)
        return (True)

    # def created_ago(self):
    #     time_ago = timezone.now() - secret.created_at


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # * my_secrets * (from related_name)
    # * liked_secrets * (from related_name)
    def __str__(self):
        return self.first_name
    objects = UserManager()

class Secret(models.Model):
    secret = models.TextField()
    creator = models.ForeignKey(User, related_name="my_secrets")  # creator of the secret; the related name 'psuedo'-creates an array of secrets for each user in the User class (not actually added to database; kept track of by Django and Python)
    likes = models.ManyToManyField(User, related_name="liked_secrets")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.secret
    objects = SecretManager()
