from django.db import models
from accounts.models import User

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=200)
    sendedBy = models.ForeignKey(User, related_name='single', on_delete=models.CASCADE, null=True)
    message = models.TextField(blank=True)


class Requests(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    account_created = models.BooleanField(default=False)
