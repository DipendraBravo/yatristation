from django.shortcuts import render, redirect
from .models import Destination
from .models import Destination_detail

# Create your views here.


def destination(request):
    destinations = Destination.objects.all()
    context={
        'destinations':destinations,
    }
    return render(request,'destination/destination.html',context)

def destination_detail(request, id):
    destination_details = Destination_detail.objects.filter(id=id).all()
    return render(request,'destination/destination_detail.html', {'dd':destination_details})

