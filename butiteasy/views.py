from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request,'index.html')

def signinpage(request):
    return render (request, 'signinpage.html')  

def signin(request):
    if request.method=='POST':
        un_name=request.POST['un_name']
        pwd=request.POST['pwd']
        user = auth.authenticate(username=un_name, password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'signinpage.html',{'showerror':'This username does not exist. Please fill in the correct details or Register.'})
    else:
        return render(request,'signinpage.html')      

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        try:
            user = User.objects.get(username=uname)
            return render(request,'signinpage.html',{'error':'This username already exists. Please try again with another username!'})
        except:
           user = User.objects.create_user(first_name=fname,last_name=lname, username=uname,password=password,email=email)    
           user.save()
           return render(request,'signinpage.html',{'msg':'You have been registered successfully!'})    
    else:
        return render(request,'signinpage.html',{'msg':'Invalid User Request...!!'})  

def logout(request):
    auth.logout(request)
    return redirect('/')          