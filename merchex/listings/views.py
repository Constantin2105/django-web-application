from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>About Us</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')

def listings(request):
    return HttpResponse('<h1>Listings</h1>')