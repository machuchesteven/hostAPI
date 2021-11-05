from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class TLD(models.Model):
    extension = models.CharField(max_length=30)
    information = models.TextField()
    base_price = models.PositiveIntegerField()
    registation_price = models.PositiveIntegerField()
    renewal_price = models.PositiveIntegerField()

    def __str__(self):
        return self.extension


class Registrant(models.Model):
    name = models.CharField(max_length=125, blank=True, null=True)
    url = models.URLField()
    tlds = models.ManyToManyField(TLD)

    def __str__(self):
        return "{self.name}"


class Domain(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True)
    registrer = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.name} registered by {self.register}"


class DomainPackage(models.Model):
    domain = models.OneToOneField(
        Domain, on_delete=models.SET_NULL, blank=True, null=True)
    offered = models.DateField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)
    registrant = models.ForeignKey(
        Registrant, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        try:
            domain = self.domain.name
            active_since = self.offered
            return f'{domain}, since: active_since'
        except e:
            return f'Domain registered but package info not  completed'


class APIKey(models.Model):
    name = models.CharField(max_length=128)
    purpose = models.CharField(max_length=256, blank=True, null=True)
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    support_link = models.URLField()

    def __str__(self):
        return self.name


# all the models regarding domian subscription
# will be added into the subscription.models
