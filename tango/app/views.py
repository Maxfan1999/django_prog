# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import Article, ForumUser
from forms import UserForm, ProfileForm, ArticleForm
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf

def article(request,id):
    context = RequestContext(request)
    context_dir = {}
    try:
        article = Article.objects.get(id = id)
        context_dir['article'] = article
        user_id = article.user_id
        user = ForumUser.objects.get(id=user_id)
        context_dir['user'] = user
    except:
        pass
    return render_to_response('article.html',context_dir,context)

def reg(request):
    context = RequestContext(request)
    reg = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            reg=True
        else: print(user_form.errors)
        print('Regirested')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        # Render the template depending on the context.
    return render(request,'register.html',{'user_form': user_form, 'profile_form': profile_form,'registered':reg},context)


def user_login(request):
    context = RequestContext(request)
    print(context)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/',context)
            else: return HttpResponse('Your account is not active')
        else:
            return HttpResponse('Invalid login details')
    else: return render(request,'login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def add_article(request):
    if request.method == "POST":
        user = request.user
        if user.is_authenticated():
            article_form = ArticleForm(data=request.POST)
            if article_form.is_valid():
                article = article_form.save()
                forum_user = ForumUser.objects.get(user = request.user)
                article.user = forum_user
                article.save()
                return HttpResponseRedirect('/')
            else: print(article_form.errors)
        else: return HttpResponse('Зарегистрируйтесь или войдите для добавления статьи')
    else:
        article_form = ArticleForm()
    return render(request,'add_article.html', {'article_form': article_form})


