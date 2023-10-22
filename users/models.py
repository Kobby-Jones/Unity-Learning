from django.db import models

# Users Model

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emaiil = models.EmailField()
    bith_date = models.DateField()
