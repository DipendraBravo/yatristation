from django.urls import path
from . import views

urlpatterns = [
    path('', views.userprofile, name="userprofile"),

    path('show_blog', views.show_blog, name="show_blog"),

]

