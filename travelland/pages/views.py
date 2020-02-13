from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Slider
from .models import Sponsor
from .models import Place


# Create your views here.


def about(request):

    return render(request, 'pages/about.html')


def destination(request):
    return render(request, 'pages/destination.html')


def destination_details(request):
    return render(request, 'pages/destination_details.html')


def blog(request):
    return render(request, 'pages/blog.html')


def contacts(request):
    return render(request, 'pages/contacts.html')


def single_blog(request):
    return render(request, 'pages/single_blog.html')


def index(request):
    slider = Slider.objects.all()
    sponsors = Sponsor.objects.all()
    don = Place.objects.all()
    return render(request, 'pages/index.html', {'sliders': slider, 'sponsor': sponsors, 'drunk': don})
