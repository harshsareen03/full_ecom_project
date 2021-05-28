from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index/index.html')


def about(request):
    return render(request, 'about/about.html')




# Create your views here.
