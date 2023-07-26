from django.shortcuts import render
from django.http import HttpResponse
from .models import Apartment

# Create your views here.

def landing_page(request):
    return render(request, 'base/landing_page.html')

def home(request):
    apartments = Apartment.objects.all()
    print(apartments)
    context = {'apartments':apartments}
    return render(request, 'base/home.html', context)