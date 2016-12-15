# coding=utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader


def authentication(request):
    title = 'Login'
    template = loader.get_template('login.html')
    text = 'Login'
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        passwd = request.POST.get('passwd', None)
        user = authenticate(username=username, password=passwd)
        if action == 'signup':
            user = User.objects.create_user(username=username, password=passwd)
            user.save()
        elif action == 'login':
            login(request, user)
        return redirect('/dashboard')
    context = {
        'title': title,
        'text': text,
    }
    return HttpResponse(template.render(context, request))

def dashboard(request):
    title = 'Hello'
    template = loader.get_template('dashboard.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))