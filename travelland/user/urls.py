from django.urls import path
from .models import HomeStay


from . import views

urlpatterns = [
    path('', views.userprofile, name="userprofile"),
    path('show_blog', views.show_blog, name="show_blog"),
    path('homestay', views.homestay, name="homestay"),
    path('home/<int:id>', views.homestay_detail, name='homestay_detail'),
    path('home/book', views.book, name="book"),
    
]