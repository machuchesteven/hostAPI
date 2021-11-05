from django import forms
from .models import *


class TLDForm(forms.ModelForm):
    class Meta:
        model = TLD
        fields = ['extension', 'information', 'base_price']


class RegistrantForm(forms.ModelForm):
    class Meta:
        model = Registrant
        fields = ""


class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = "__all__"


class DomainPackageForm(forms.ModelForm):
    class Meta:
        model = Registrant
        fields = ["domain", "active"]


class APIKeyForm(forms.Form):
    class Meta:
        model = APIKey
        fields = "__all__"
