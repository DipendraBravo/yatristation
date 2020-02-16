from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Post
from .models import UserProfile
from .models import HomeStay
from .models import Book 




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

def homestay(request,*args,**kwargs):
    homestay = HomeStay.objects.all()
    user = User()
    if request.method == 'POST':
        getestimation = request.POST['getestimation']
        homestayname = request.POST['homestayname']
        popularamenitities = request.POST['popularamenitities']
        price = request.POST['price']
        pricedetail = request.POST['pricedetail']
        location = request.POST['location']
        pannumber = request.POST['pannumber']
        foodanddrinks = request.POST['foodanddrinks']
        guestservice = request.POST['guestservice']
        outdoors = request.POST['outdoors']
        accessibility = request.POST['accessibility']
        homestaypicture = request.FILES['picture_main']
        room1pic = request.FILES['room1pic']
        room2pic = request.FILES['room2pic']
        outdoorpic = request.FILES['outdoorpic']
        citizenshipfront = request.FILES['citizenshipfront']
        citizenshipback = request.FILES['citizenshipback']
        post = HomeStay(getestimation=getestimation, homestayname=homestayname,
        popularamenitities=popularamenitities,price=price, pricedetail=pricedetail, location=location, 
        pannumber=pannumber, foodanddrinks=foodanddrinks, guestservice=guestservice,
        outdoors=outdoors, accessibility=accessibility,homestaypicture=homestaypicture,
        room1pic=room1pic, room2pic=room2pic,outdoorpic=outdoorpic, 
        citizenshipfront=citizenshipfront,
        citizenshipback=citizenshipback)
        post.user = request.user
        post.save()
        return redirect('/')
    else:
        return render(request, 'user/homestay.html', {'title': 'HomeStay| YatriStation', 'homestay': homestay})

def homestay_detail(request,id):
    homestay_detail = HomeStay.objects.filter(id=id).all()
    return render(request,'user/homestaydetails.html', {'dd': homestay_detail})

def book(request,*args,**kwargs):
    # homestayid = HomeStay()
    user = User()
    if request.method == 'POST':
        guestname = request.POST['guestname']
        guestcontact = request.POST['guestcontact']
        guestemail = request.POST['guestemail']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        noofguest = request.POST['noofguest']
        reasonforbooking = request.POST['reasonforbooking']
        update = Book(guestname=guestname, guestcontact=guestcontact, guestemail=guestemail,
        startdate=startdate,enddate=enddate,noofguest=noofguest,reasonforbooking=reasonforbooking)
        update.user = request.user
        # update.homestayid = request.homestayid
        update.save()

        return redirect('/')
    else:
         return render(request, 'user/book.html')
 


