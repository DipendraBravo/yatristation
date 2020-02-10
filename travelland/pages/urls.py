
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destination', views.destination, name='destination'),
    path('destination_details', views.destination_details, name='destination_details'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contacts'),
    path('single_blog', views.single_blog, name='single_blog'),
     path('signin', views.signin, name='signin'),
    path('signup',views.signup,name='signup'),
    
]