from django.urls import path
from user import views
urlpatterns = [
    path('/login', views.loginFun),
    path('/register', views.register),
    path('/logout', views.logoutFun),
    path('/contact', views.contact),
    
]
