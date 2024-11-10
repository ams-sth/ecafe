from django.shortcuts import redirect, render

from user import views
from item.models import Item

# Create your views here.

def index(request):

    items = Item.objects.all()
    return render(request, 'user/ecafe.html', {'items': items})


