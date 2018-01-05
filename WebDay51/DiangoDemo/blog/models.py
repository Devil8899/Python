from django.db import models

# Create your models here.
#
class User(models.Model):
    name=models.CharField(max_length=64)
    email=models.CharField(max_length=64)
    mobile=models.CharField(max_length=64)
    address=models.CharField(max_length=64)