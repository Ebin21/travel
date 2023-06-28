from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    return render(request, "login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


def registration(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        passw=request.POST['password']
        cpass=request.POST['cPassword']

        if passw==cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username is Taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id is  Taken")
                return redirect('registration')
            else:
                user=User.objects.create_user(username=uname,password=passw,first_name=fname,last_name=lname,email=email)
                user.save()
                return render(request, "login.html")
        else:
            messages.info(request, "Password isn't matching")
            return redirect('registration')
        return redirect('/')

    return render(request, "reg.html")