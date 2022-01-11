from login_register.models import create_user
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
import bcrypt
from .models import *
def index(request):
    return render(request,"index.html")

def register(request):
    errors = users.objects.register(request.POST)
    if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    first_name= request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']
    if password == confirm_password:
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = create_user(first_name,last_name,email,password)
        request.session['id']= user.id
        request.session["first_name"]= user.first_name
        request.session["last_name"]= user.last_name
    return redirect('/sucsess')

def sucsess(request):
    # context={
    #         'reguser': users.obects.get(id=request.session["id"])
    #      }
    return redirect('/book')

def login(request):
    if request.method =="POST":
        errors = users.objects.login(request.POST)
        if len(errors)>0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
        email = request.POST['email']
        password = request.POST['password']
        user = get_user(email,password)
        if user:
                request.session["id"]= user.id
                request.session["first_name"]= user.first_name
                request.session["last_name"]= user.last_name
                return redirect("/welcome")
    return redirect('/')
def welcome(request):

        return redirect('/book')


def logout(request):
    request.session.clear()

    return redirect('/')

    