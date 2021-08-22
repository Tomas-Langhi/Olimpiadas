import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Count
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
import datetime
from django import forms
from django.contrib import messages

from django.db.models.fields.related import ManyToManyField

# Create your models here.

class PeopleIn(models.Model):
    countIn = models,IntegerField(default=0, verbose_name_plural= "countsIn")
    timeIn = models.DateTimeField(verbose_name_plural= "timesIn")

    def AddIn(countIn, timeIn):
        countIn += 1
        timeIn = datetime.datetime.now()

    class Meta:
        verbose_name_plural = ["PeopleIn"]
        

class PeopleOut(PeopleIn):
    countOut = models,IntegerField(default=0, verbose_name_plural= "countsOut")
    timeOut = models.DateTimeField(verbose_name_plural= "timesOut")

    def AddOut(countOut,timeOut):
        countOut += 1
        timeOut = datetime.datetime.now()

    class Meta:
        verbose_name_plural = ["PeopleOut"]


class PeopleCount(PeopleOut):
    count = models.IntegerField(default=0)
        
    class Meta:
        verbose_name_plural = ["PeoplesCount"]

class Country(models.Model):
    countyOptions = (
        (1, "Argentina"),
        (2, "Brasil"),
    )

    name = forms.ChoiceField(countyOptions)



class City(Country):
    name = models.CharField(max_length=20, default="")
    
    if Country.name == 1:
        cityOptions = (
        (1, "Cordoba"),
        (2, "Buenos Aires"),    
        )

    elif Country.name == 2:
        cityOptions = (
            (3, "Brasilia"),
            (4, "Rio do Jaeiro"),    
        )
    else:
        messages.warning("Primero seleccione un pais")

class Street(City):
    
    name = models.CharField(max_length=20, default="")

class Localization(models.Model):
    country = forms.ChoiceField()
    city = models.CharField(max_length=20, default="")
    street = models.CharField(max_length=20, default="")

class Subsidiary(models.Model):
    name = models.CharField(max_length=20, default="")
    localization = ManyToManyField(Localization, null=True, on_delete=CASCADE)    

