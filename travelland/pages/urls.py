from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destination', views.destination, name='destination'),
    path('signin', views.signin, name='signin'),
    path('signup',views.signup,name='signup'),
]
