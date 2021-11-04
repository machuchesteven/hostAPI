from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL)
