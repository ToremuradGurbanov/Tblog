from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterFrom
from theblog.models import ConnectedUser
# Create your views here.

def register(response):
    if response.method =='POST':
        form = RegisterFrom(response.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')
    
    form = RegisterFrom()
    context = {'form':form}
    
    return render(response, 'register/register.html', context)




def profile(response):
    objects= ConnectedUser.objects.all()
    context = {'objects': objects}
    return render(response, 'register/profile.html', context)
