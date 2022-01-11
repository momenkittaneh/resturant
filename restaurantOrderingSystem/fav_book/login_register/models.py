from django.db import models
import re
class userModels(models.Manager):
    def register(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors["first_name"] = "first name should be at least 2 characters and contains only characters"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors["last_name"] = "last name should be at least 2 characters and contains only characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters atleast"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        return errors

    def login(self, postData):
        errors = {}
        email = postData['email']
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters atleast"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if not EMAIL_REGEX.match(email):
            errors["email"] = "Email isn't in database"
        return errors

class users(models.Model):
    first_name= models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password= models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= userModels()


def create_user(fname,lname,email,passwd):
    user = users.objects.create(first_name=fname,last_name=lname,email=email,password=passwd)
    return user

def get_user(email,passwd):
    user=users.objects.filter(email=email,password=passwd)
    #[0] to select only one user for the email and password
    if len(user) > 0:
        return user[0]
    return False

def return_user(id):
    user= users.objects.get(id=id)
    return user

def get_user_cars(id):
    user= users.objects.get(id=id)
    return user
