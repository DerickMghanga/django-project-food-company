from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Little Lemon Restaurant !")

def say_hello(request):
    return HttpResponse("Hello there")

def little_lemon(request):
    return HttpResponse("Best restaurant in Nairobi")