from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Slider
from .models import Sponsor


# Create your views here.
def index(request):
    slider = Slider.objects.all()
    sponsors = Sponsor.objects.all()

    return render(request, 'pages/index.html', {'sliders': slider, 'sponsor': sponsors})


def about(request):
    return render(request, 'pages/about.html')


def destination(request):
    return render(request, 'pages/destination.html')

