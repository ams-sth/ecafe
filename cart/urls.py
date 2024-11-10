from django.urls import path
from cart import views
urlpatterns = [
    path("/cartShow/<int:id>", views.show,),]