from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#class Consumer(models.Model):
#    user=models.OneToOneField(User,on_delete=models.CASCADE)

class user(models.Model):
    email=models.EmailField()
    username=models.CharField(max_length=100)