from rest_framework.serializers import HyperlinkedModelSerializer
from .models import *


class DomainSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class DomainSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class DomainPackageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = DomainPackage
        fields = ["domain", "active"]


class APIKeySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = APIKey
        fields = "__all__"
