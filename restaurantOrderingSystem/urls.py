from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from . import forms
urlpatterns =[
    path('', login_required(views.index)),
    path('insert', views.insert),
    path('createuser',views.CreateUser),
    path('menu', views.menu),
    path('addfood/<int:id>', views.AddToFood),
    path('food', views.food),
    path('makeorder', views.makeorder),
    path('yourorder', views.food2),
    path('orders', login_required(views.order.as_view())),
    path('kitchen', login_required(views.kitchen)),
    path('orders/<int:id>', login_required(views.orderdetail)),
    path('kitchen/<int:id>', login_required(views.kitchendetail)),
    path('accounts/login/', views.Login.as_view(template_name="login.html",authentication_form=forms.UserLoginForm)),
    path('logout', views.Logout.as_view()),
    path('choose', views.choose),
    path('update/PREPARING/<int:id>/<int:coid>', views.preparing),
    path('update/done/<int:id>/<int:coid>', views.done),
    path('update/deliver/<int:id>/<int:coid>', views.deliver),

]