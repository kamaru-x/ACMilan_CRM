from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def sign_in(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('.')
    return render(request,'login.html')


@login_required
def dashboard(request):
    return render(request,'index.html')