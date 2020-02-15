from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from user.models import Notification

# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            n = Notification.objects.filter(user=request.user,viewed=False)
            return render_to_response("userprofile",{'notifications':n})

        else:
            messages.info(request, 'invalid credentials')
            return redirect("login")
    else:
        return render(request, 'form/signin.html', {'title': 'Login | YatriStation'})


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'Welcome to Yatri Station')
                return redirect("login")
        else:
            messages.info(request, 'password not matching')
        return redirect("signup")
    else:
        return render(request, 'form/signup.html', {'title': 'Register | YatriStation'})


def logout(request):
    auth.logout(request)
    return redirect('/')
