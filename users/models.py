from django.db import models

# Users Model
class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emaiil = models.EmailField()
    bith_date = models.DateField()
    

    def __str__(self):
        return f" {self.first_name} {self.last_name} "

# Courses Model
class Courses(models.Model):
    course_title = models.CharField(max_length=200)
    course_category = models.CharField(max_length=200)
    course_image = models.ImageField()
    course_views = models.BigIntegerField()

    def __str__(self):
        return f" {self.course_title} | Views: {self.course_views} "