from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def home(request): 
    # current_user=request.user
    # user_id='current_user_id'
    # print(user_id)
    # context={
    #     'user_id':user_id
    # }
    fullname =  request.user.get_full_name()
    context = {'fullname':fullname}
    return render(request,'Home.html',context)


def signup(request):
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
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
    
    
@login_required(login_url='/login')
    
def logout(request):
    auth.logout(request)
    return redirect('/login')

def yourinformation(request):
    return render(request,'Your_information.html')

