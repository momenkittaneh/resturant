from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #show main page
    path('register',views.register), #for the regiseration
    path('sucsess',views.sucsess),
    path('login',views.login), #for the login page
    path('welcome',views.welcome),
    path('logout',views.logout),
    
    
]
