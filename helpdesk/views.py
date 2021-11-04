from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.mail import send_mail, send_mass_mail
# Create your views here.


class Home(View):
    def get(self, request):
        return HttpResponse("The customer help desk is under construction")


class SendMail(View):
    def get(self, request):
        message_body = "Hello"
        send_mail("Message name", "message bidy",
                  "example@gmail.com", ["receiver@gmail.com"])
        return HttpResponse("<h1>Email Sent</h1>")
