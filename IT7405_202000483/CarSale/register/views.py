from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"User already exists")
                return render(request, 'register/register.html') 
                
               
                
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('carview:homePage')
        else:
            messages.error(request,"password mismatch")
            return render(request, 'register/register.html')
            
       
        
    else:
        return render(request, 'register/register.html')