# coding=utf-8

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def authentication(request):
    title = 'Login'
    template = loader.get_template('login.html')
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            user = request.POST['username']
            passwd = request.POST['password']
            request.session['user_s'] = user
            access = authenticate(username=user, password=passwd)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    url = 'userprofiles:dashboard'
                    return HttpResponseRedirect(reverse(url))
                else:
                    text = 'El usuario no esta Activo'
                    contextNoActive = {
                        'text': text,
                        'form': form,
                        'title': title,
                    }
                    return HttpResponse(template.render(contextNoActive, request))
            else:
                text = 'El usuario o la contraseña son incorrectos'
                contextNoUser = {
                    'text': text,
                    'form': form,
                    'title': title,
                }
                return HttpResponse(template.render(contextNoUser, request))

    else:
        form = AuthenticationForm()
    text = ""
    context = {
        'title': title,
        'form': form,
        'text': text,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def dashboard(request):
    title = 'Sistema de Pares Evaluadores'
    template = loader.get_template('dashboard.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))

# def authentication(request):
#     title = 'Login'
#     template = loader.get_template('login.html')
#     text = 'Login'
#     if request.method == 'POST':
#         action = request.POST.get('action', None)
#         username = request.POST.get('username', None)
#         passwd = request.POST.get('passwd', None)
#         user = authenticate(username=username, password=passwd)
#         if action == 'signup':
#             user = User.objects.create_user(username=username, password=passwd)
#             user.save()
#         elif action == 'login':
#             login(request, user)
#         return redirect('/dashboard')
#     context = {
#         'title': title,
#         'text': text,
#     }
#     return HttpResponse(template.render(context, request))