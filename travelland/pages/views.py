from django.shortcuts import render, redirect
from .models import Slider
from .models import Sponsor
from .models import PopularPlaces
from .models import Hotel


# Create your views here.


def contacts(request):
    return render(request, 'pages/contacts.html')


def single_blog(request):
    return render(request, 'pages/single_blog.html')


def index(request):
    slider = Slider.objects.all()
    sponsors = Sponsor.objects.all()
    popularplaces = PopularPlaces.objects.all()
    hotels = Hotel.objects.all()
    return render(request, 'pages/index.html',
                  {'sliders': slider, 'sponsor': sponsors, 'popularplaces': popularplaces, 'hotels': hotels})
