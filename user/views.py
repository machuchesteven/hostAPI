from django.shortcuts import render
from django.contrib.auth.views import login, authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class CreateUserView(View):
    def post(self, request):
        pass


class LoginView():
    pass
