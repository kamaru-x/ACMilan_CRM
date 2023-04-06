from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # user modes
    is_district_coordinator = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)
    is_centre = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    # Additional Data
    Center1 = models.CharField(max_length=50,null=True)
    Center2 = models.CharField(max_length=50,null=True)
    Mobile = models.CharField(max_length=15,null=True)
    Mobile2 = models.CharField(max_length=15,null=True)
    Address = models.CharField(max_length=50,null=True)