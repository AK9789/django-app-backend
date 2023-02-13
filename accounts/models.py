from django.db import models
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.
    # print(random.randint(123123123123,947258369125))

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length= 100)
    branch = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    account_number = models.IntegerField(default=random.randint(123123,947258), blank=True)
    balance = models.IntegerField(default=1200, blank=True)
 