from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()




# Create your models here.
class reg(models.Model):
    name =models.CharField(max_length=255,blank=False)
    username = models.CharField(max_length=255,blank=False)
    password = models.CharField(max_length=255,blank=False)
    c_password = models.CharField(max_length=255,blank=False)
