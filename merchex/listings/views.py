from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

# Create your views here.



def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
    {'bands': bands})

def about(request):
     return render(request, 'listings/about.html')

def contact(request):
    return render (request, 'listings/contact.html')

def listings(request):
    return render(request, 'listings/listings.html')