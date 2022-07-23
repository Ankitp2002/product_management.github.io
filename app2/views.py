from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def productview(request):
    return HttpResponse("welcome to web sit")