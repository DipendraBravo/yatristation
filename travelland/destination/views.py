from django.shortcuts import render, redirect
from .models import Destination

# Create your views here.


def destination(request):
    destinations = Destination.objects.all()
    context={
        'destinations':destinations,
    }
    return render(request,'destination/destination.html',context)
