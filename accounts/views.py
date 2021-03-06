
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login_view(request): 
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')   
        try: 
            if '@' in username:
                user_obj = User.objects.get(email=username)
                username = user_obj.username
        except:    
            return HttpResponseRedirect(reverse('accounts:login'))

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    form = AuthenticationForm()        
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your account created successfully")
            return HttpResponseRedirect(reverse('accounts:login'))

    form = UserCreationForm()
    context = {"form":form}

    return render(request, 'accounts/signup.html', context)