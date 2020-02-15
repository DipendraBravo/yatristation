from django.urls import path
from . import views
from .models import Destination

urlpatterns = [
	path('', views.destination, name='destination'),
	path('dest/<int:id>', views.destination_detail, name='destinationdetail'),
]