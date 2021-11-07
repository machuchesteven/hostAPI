from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('service', ServiceView, basename="service")


urlpatterns = [
    path('', include(router.urls)),
]
