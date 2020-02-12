from django.shortcuts import render, redirect
from .models import Tourplan
from .models import Ourstory
from .models import ProjectPartner
# Create your views here.


def about(request):
    ourstories = Ourstory.objects.all()
    tourplans = Tourplan.objects.all()
    projectpartners = ProjectPartner.objects.all()
    context={
        'ourstories':ourstories,
        'tourplans':tourplans,
        'projectpartners':projectpartners,
    }
    return render(request,'about/about.html',context)

