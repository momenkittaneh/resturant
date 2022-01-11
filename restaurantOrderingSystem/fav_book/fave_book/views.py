from login_register.models import users
from fave_book.models import *
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

def hello(request):
    context={
        "listbook" :books.objects.all(),
        'favbook'  : get_fav_book(request.session['id'])
    }
    return render(request,'fav.html',context)

def addbook(request):
    title = request.POST['title']
    desc =request.POST['desc']
    add_book=create_book(title,desc,request.session['id'])
    return redirect('/book')

def addfav(request,id):
        add_fav(id,request.session['id'])
        return redirect('/book')

def displaybook(request,id):
    book = books.objects.get(id =id)
    owner = book.uploaded_by.id
    if (request.session['id'] == owner):
        context={
            'books' : books.objects.get(id =id),
            'user'  : book.fave.all(),
            'owner'  : request.session['id'],
            'book'   : book.uploaded_by

        }
        return render(request,'edit.html',context)
    else:
        context={
            'books' : books.objects.get(id =id),
            'user'  : book.fave.all(),
            'owner'  : request.session['id'],
            'book'   : book.uploaded_by

        }
        return render(request,"info.html",context)
def update(request,id):
    desc = request.POST['desc']
    update_book(id,desc)
    return redirect('/book')

def delet(requist,id):
    del_book =books.objects.get(id = id)
    del_book.delete()
    return redirect('/book')
