from django.urls import path
from .views import *

app_name = 'helpdesk'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('/sendmail', SendMail.as_view(), name='sendmail')
]
