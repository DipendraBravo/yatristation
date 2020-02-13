from django.urls import path
from . import views
from .models import Destination_detail

urlpatterns = [
	path('', views.destination_detail, name='destination_detail'),
]