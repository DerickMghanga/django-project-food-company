from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Welcome to the Little Lemon Restaurant !")

def say_hello(request):
    return HttpResponse("Hello there")

def little_lemon(request):
    return HttpResponse("Best restaurant in Nairobi")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14">This is Little lemon again</h1>"""
    return HttpResponse(text)