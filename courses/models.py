from django.db import models


# Couses model
class Courses(models.Model):
    course_title = models.CharField(max_length=200)
    course_description = models.TextField()
