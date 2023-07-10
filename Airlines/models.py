import email
from enum import auto
from http import client
from pyexpat import model
from random import random
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.forms import EmailField, PasswordInput
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=80)

class Flight(models.Model):
    Flight_no = models.CharField(max_length=30, primary_key = True)
    Flight_model = models.CharField(max_length=30)
    capacity = models.IntegerField()
    def __str__(self):
        return self.Flight_no

class Voyage(models.Model):
    voyid= models.CharField(max_length=20, primary_key= True)
    From = models.CharField(max_length=30)
    To = models.CharField(max_length=30)
    departure = models.DateTimeField()
    Flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
    def __str__(self):
        return self.voyid


class Reserve(models.Model):
    client = models.ForeignKey("User", on_delete=models.CASCADE)
    voy = models.ForeignKey("Voyage", on_delete=models.CASCADE)

