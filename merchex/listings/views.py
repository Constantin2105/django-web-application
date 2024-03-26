from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

# Create your views here.



def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html')

def about(request):
    return HttpResponse('<h1>About Us</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')

def listings(request):
    return HttpResponse('<h1>Listings</h1>')