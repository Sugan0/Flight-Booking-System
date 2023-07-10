from ast import Num
import email
from email import message
from hmac import trans_36
from imaplib import _Authenticator
from logging import error
from multiprocessing import AuthenticationError, dummy
from platform import uname
from pydoc import cli
from re import template
from telnetlib import AUTHENTICATION
from unittest import loader
from urllib import request
from django import views
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Now
import os
import pdfkit
from django.contrib import messages

from Airlines import forms

from .models import Reserve, User, Voyage
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request, 'index.html')

def save(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        email2 = request.POST['email']
        phone3 = request.POST['phone']
        password2 = request.POST['password']
        if User.objects.filter(username=username2).exists():
                messages.info(request, "Username Already Exists!")
                return redirect('SignUp')
        elif User.objects.filter(email=email2).exists():
                messages.info(request, "Email Already Exists!")
                return redirect('SignUp')
        client = User(username=username2, email=email2, password=password2, phone=phone3)
        client.save()
        return redirect ('login')
    return render(request, 'signup.html')

def home(request):
    return render(request, 'index.html')



def signin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            #start a session for the current user
            request.session['User'] = uname
            return redirect('profile')
        else:
            msg = "Wrong Username or password!"
            return render(request, 'signin.html', {'msg': msg})

    return render(request, 'signin.html')

def reservations(request):
    if 'User' in request.session:
        uname2 = request.session['User']
        c = User.objects.get(username = uname2)
        reserve = Reserve.objects.filter(client = c)
        if request.method == 'GET':
            voyageid = request.GET.get('voyid')
            if voyageid is not None:
                v = Voyage.objects.get(voyid = voyageid)
                r = Reserve(client = c, voy = v)
                r.save()
        return render (request, 'reservation.html', {'reserve': reserve, 'uname2':uname2})
    else:
        return render(request, 'signin.html')

def profile(request):
    if 'User' in request.session:
        current_user = request.session['User']
        param = {'current_user': current_user}
        return render(request, 'profile.html', param)
    else:
        return redirect('login')
    return render(request, 'signin.html')


def logout(request):
    try:
        del request.session['User']
    except:
        return redirect('login')
    return redirect('login')

def flights(request):
    if request.method == 'POST':
        From1 = request.POST.get('From1')
        To1 = request.POST.get('To1')
        departure = request.POST.get('date')
        
        data = Voyage.objects.filter(From = From1, To = To1) #filter only the trips that are not expired
    
        return render (request, 'flights.html', {  'voy': data})
    return render (request, 'flights.html')

    

def admin1(request):
    return redirect('http://127.0.0.1:8000/admin/login/?next=/admin/')

