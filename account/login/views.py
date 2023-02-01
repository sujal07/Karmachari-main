from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

def home(request):
    return render(request,'Home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        print (request.POST['username'])
        username=request.POST['username']
        password=request.POST['password']
        User=auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            return redirect('/login')
    else: 
        return render(request,'login.html')