from django.shortcuts import render, redirect
from .models import Destination_detail
from destination.models import Destination
# Create your views here.


def destination_detail(request):
    destination_details = Destination_detail.objects.all()
    context={
        'destination_details':destination_details,
    }
    return render(request,'destination_detail/destination_detail.html',context)
