from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *


def index(request):
    context = {}

    return render(request, 'index.html', context)


def signup(request):
    context = {}
    return render(request, 'signup.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect('index')


def login_request(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:  # verificando se usuario esta bloqueado
                login(request, user)
                return redirect('index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'error.html', context)


def logout_request(request):
    logout(request)
    return redirect('index')
