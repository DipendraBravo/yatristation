from django.urls import path

from . import views

urlpatterns = [
    path('', views.userprofile, name="userprofile"),
    path(r'^show/(?p<notification_id>/d+}/$',views.notification,name='show_notification'),
    path(r'^delete/(?p<notification_id>/d+}/$',views.notification,name='delete_notification'),
    path('show_blog', views.show_blog, name="show_blog"),


]
