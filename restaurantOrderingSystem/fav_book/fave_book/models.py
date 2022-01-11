from django.db.models.deletion import CASCADE
from django.shortcuts import redirect
from login_register.models import users
from django.db import models
from login_register.models import *


class books(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    uploaded_by =models.ForeignKey(users,related_name='owner',on_delete=CASCADE)
    fave = models.ManyToManyField(users,related_name='favebook')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





def create_book(title,desc,id):
    ownedby=users.objects.get(id=id)
    book=books.objects.create(title=title,desc=desc,uploaded_by=ownedby)
    ownedby.favebook.add(book)
    return book



def get_fav_book(user_id):
    user = users.objects.get(id= user_id)
    return user.favebook.all()



def add_fav(book_id,user_id):
    book= books.objects.get(id = book_id)
    user = users.objects.get(id=user_id)
    user.favebook.add(book)


def update_book(id,desc):
    book= books.objects.get(id = id)
    book.desc =desc
    book.save()
    return True