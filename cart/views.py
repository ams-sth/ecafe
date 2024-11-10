from django.shortcuts import render
from cart.models import Cart
from item.models import Item
from cart.forms import CartForm

# Create your views here.

def show(request, id):
    items = Item.objects.get(id=id)
    return render(request, "cart/cart.html", {'items':items})