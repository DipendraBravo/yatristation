
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destination', views.destination, name='destination'),

    path('destination_details', views.destination_details, name='destination_details'),

    path('contacts', views.contacts, name='contacts'),
    path('single_blog', views.single_blog, name='single_blog'),
    
    
]

