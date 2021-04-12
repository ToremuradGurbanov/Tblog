from django.shortcuts import render
from django.http import HttpResponse
from .models import ConnectedUser

# Create your views here.
def homepage(response):
    objects = ConnectedUser.objects.all()
    form = ConnectedUser
    context  = {'form':form}
    return render(response, 'theblog/homepage.html', context)