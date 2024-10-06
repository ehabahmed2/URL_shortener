from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import UrlInfo
import random
import string
from .forms import RegisterUser, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages



def main(request):
    if request.method == 'POST':
        url = request.POST.get('original_url')
        existing_url = UrlInfo.objects.filter(url=url).first()
        if existing_url:
            short_url = request.build_absolute_uri('/u/') + existing_url.short_url
            urls = UrlInfo.objects.all() if request.user.is_authenticated else None
            context = {
                'short_url': short_url,
                'urls': urls,
                'base_url': request.build_absolute_uri('/u/'),
            }
            return render(request, 'index.html', context)
        
        short_code = generate_code()
        short_url = request.build_absolute_uri('/u/') + short_code
        
        try:
            user = request.user if request.user.is_authenticated else None
            UrlInfo.objects.create(url=url, short_url=short_code, user=user)
        except IntegrityError:
            short_code = generate_code()
            short_url = request.build_absolute_uri('/u/') + short_code
            UrlInfo.objects.create(url=url, short_url=short_code, user=user)
        
        urls = UrlInfo.objects.all() if request.user.is_authenticated else None
        context = {
            'short_url': short_url,
            'urls': urls,
            'base_url': request.build_absolute_uri('/u/'),
        }
        return render(request, 'index.html', context)
    
    else:
        short_url = 'Short URL'
        urls = UrlInfo.objects.all() if request.user.is_authenticated else None
        context = {
            'short_url': short_url,
            'urls': urls,
            'base_url': request.build_absolute_uri('/u/'),
        }
        return render(request, 'index.html', context)



def generate_code():
    chrs = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choices(chrs, k=5))
        if not UrlInfo.objects.filter(short_url=short_code).exists():
            break
    return short_code

def urlRedirect(request, short_url):
    print(f"Received short_url: {short_url}")
    url_info = UrlInfo.objects.filter(short_url=short_url).first()
    if url_info:
        url_info.clicks += 1
        url_info.save()
        return redirect(url_info.url)
    else:
        return render(request, '404.html', status=404)


def register_user(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()  # Save user as a regular user
            login(request, user)  # Log in the user
            messages.success(request,'User registered Succesfully')
            return redirect('main')  # Redirect after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterUser()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in!')
                return redirect('main')  # Redirect after successful login
            else:
                messages.error(request, 'Invalid email or password!')
    else: 
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('main')  # Replace 'main' with the name of your home page view