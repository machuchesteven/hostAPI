from django.db import models
from domain.models import DomainPackage, Domain
# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="services",
                              default="default_service.png")

    def __str__(self):
        return self.name


class PaymentOption(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    used_since = models.DateField(auto_now=True, editable=False)
    modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Payment Via {self.name}'

# defining custom packages


class Bundle(models.Model):
    name = models.CharField(max_length=15)
    duration = models.DurationField(blank=True, null=True)
    # here the currency used is in dollars and the conversion will take place but will be managed
    price = models.PositiveIntegerField()
    offering_since = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.name} for $ {self.price}'


class DomainBundle(models.Model):
    domain_package = models.OneToOneField(
        DomainPackage, on_delete=models.CASCADE)
    bundle = models.ForeignKey(
        Bundle, null=True, blank=True, on_delete=models.SET_NULL)


class HostingBundle(models.Model):
    pass


class EmailBundle(models.Model):
    pass
