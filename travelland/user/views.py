from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Post
from .models import UserProfile
from django.shortcuts import render_to_response
from django.http import HttpResponstedRedirect
from .models import Notification


# Create your views here.


def userprofile(request,*args, **kwargs):

    userone = UserProfile.objects.filter(user_id=request.user.id).all()
    user = User()

    if request.method == 'POST':
        gender = request.POST['gender']
        contact = request.POST['contact']
        address = request.POST['address']
        guider = request.POST['guider']
        update = UserProfile(gender=gender, contact=contact, address=address,guider=guider)
        update.user = request.user
        update.save()


    return render(request, 'user/user.html', {'userone':userone})


def show_blog(request):
    all_blog = Post.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        title = request.POST['title']
        blog_pic = request.FILES['blog_pic']

        description = request.POST['description']
        post = Post(user_name=username, title=title, blog_pic=blog_pic, description=description)
        post.save()
        return redirect('/')
    else:
        return render(request, 'blog/blog.html', {'title': 'Blog| YatriStation', 'blog': all_blog})

def show_notification(request, Notification_id):
    n = Notification.objects.get(id=notification_id)
    return render_to_response('user/user.html',{'notification':n})

def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()

    return HttpResponstedRedirect('/account/login')