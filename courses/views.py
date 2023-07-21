from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def courses (request) :
    return HttpResponse("welcome to dajngo")