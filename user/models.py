from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# class Admin(models.Model):
#     id=models.AutoField(auto_created=True, primary_key=True)
#     firstname=models.CharField(max_length=255)
#     middlename=models.CharField(max_length=255)
#     lastname=models.CharField(max_length=255)
#     username=models.CharField(max_length=255)
#     email=models.EmailField(max_length=255)
#     password=models.CharField(max_length=20)
#     address=models.CharField(max_length=255)
#     phonenumber=models.CharField(max_length=10)

class Login(models.Model):
     id=models.AutoField(auto_created=True, primary_key=True)
     username=models.CharField(max_length=255)
     password=models.CharField(max_length=20)

class Register(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    firstname=models.CharField(max_length=255)
    middlename=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=10)
