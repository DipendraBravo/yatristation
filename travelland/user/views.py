from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Post


# Create your views here.


def userprofile(request):
    return render(request, 'user/user.html')


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
