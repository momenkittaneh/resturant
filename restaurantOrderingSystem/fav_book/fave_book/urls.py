from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello), #show main page
    path('addbook',views.addbook),
    path('addtofav/<int:id>',views.addfav),
    path('book/<int:id>',views.displaybook), 
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delet)
]