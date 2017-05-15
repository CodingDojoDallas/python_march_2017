from __future__ import unicode_literals
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.CharField(max_length = 400, default = 'N/A')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):      # By default return the course name
		return self.name

# # Make Description a one-to-one relationship with the Course table rather than a column
# class Description(models.Model):
#     course = models.OneToOneField(Course, related_name = 'desc')
#     text = models.TextField(default = 'N/A')
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#
#     def __str__(self):      # By default return the description text
# 		return self.text
#
# # Add comments about the courses that will be rendered on a separate page
# class Comment(models.Model):
#     course_id = models.ForeignKey(Course, related_name = 'comments')
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#
#     def __str__(self):      # By default return the comment text
# 		return self.text
