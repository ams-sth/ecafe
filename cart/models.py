from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from item.models import Item


class Cart(models.Model):
    cartId=models.AutoField(auto_created=True, primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    id  = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()


        
    class meta:
        db_table="cart"

