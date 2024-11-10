from django.db import models



class Item(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    name=models.CharField(max_length=255 )
    brand=models.CharField(max_length=255 ,blank=True )
    price=models.FloatField(default=0,blank=True)
    image=models.ImageField(upload_to='static/images', default='default.jpg')  

    class meta:
        db_table="Item"



