from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class BundleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bundle
        fields = "__all__"
