from django.db import models
from django.contrib.auth.models import User, Group
from helpdesk.models import DaySupervisor, SupportPersonnel

# Create your models here


class Profile(models.Model):
    # can be made the attrinbute since it only have one instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='users/pic', default="default.png")

    def picture(self):
        try:
            picture_url = self.pic.url
            return picture_url
        except e:
            return ""

    def __str__(self):
        try:
            first_name = self.user.first_name
            last_name = self.user.last_name
            return f'Profile for {self.user.username}'
        except e:
            return "Profile Information are not accurate, Complete them and come back"


class Customer(models.Model):
    # here we will know if we are dealing with an enterprise of an individual
    customer_type = models.CharField(max_length=20, blank=True, null=True)
    support_personnel = models.ForeignKey(
        SupportPersonnel, on_delete=models.CASCADE)
    information = models.TextField()


class CustomerLog(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    services = models.CharField(max_length=256)
