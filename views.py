from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#import model
from . models import reg

# Create your views here.


#contact-us  page  function
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('cpassword')
       
        
        #send data for model and store in database
        d = reg() # d:- means details of all data
        d.name=name
        d.username = username
        d.password=password
        d.c_password = c_password
        
        #save the object in databse
        d.save()
        # return redirect("login/")
    else:
        
        return render(request,'contactus.html')
  
    

#login pagefunction
def login(request):
    if request.method =='POST':
        user_name = request.POST['username']
        password = request.POST['password']
        
        #match username and password in database
        user = auth.authenticate(username = user_name, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home/')
        else:
            messages.info(request,"login invalid")
            return redirect('/login/')
    else:
        
        return render(request,'login.html')

#logout

@login_required(login_url='login')  
def logout(request):
    auth.logout(request)
    return redirect('/')
    return render(request,'logout.html')
    


#home page  function
def home(request):
    return render(request,'home.html')



#all food product details function
def details(request):
    return render(request,"details.html")


def details2(request):
    return render(request,"details2.html")
def cong(request):
    return render(request,'payment.html')
