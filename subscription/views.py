from django.shortcuts import render
from django.views import View
from .serializers import *
from .models import *


from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ServiceView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "pk"


class BundleView(ModelViewSet):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer
    lookup_field = "pk"
