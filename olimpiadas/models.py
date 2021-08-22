import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Count
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import CharField, IntegerField
import datetime
from django import forms
from django.contrib import messages

from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Responsable(models.Model):
    name = models.CharField(max_length=30, default="")
    lastName = models.CharField(max_length=30, default="")
    dni = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name

class CountIn(models.Model):
    countIn = models,IntegerField(default=0, verbose_name_plural= "countsIn")
    timeIn = models.DateTimeField(verbose_name_plural= "timesIn")

    def AddIn(countIn, timeIn):
        countIn += 1
        timeIn = datetime.datetime.time.now()

    class Meta:
        verbose_name_plural = ["PeopleIn"]
        

class CountOut(PeopleIn):
    countOut = models,IntegerField(default=0, verbose_name_plural= "countsOut")
    timeOut = models.DateTimeField(verbose_name_plural= "timesOut")

    def AddOut(countOut,timeOut):
        countOut += 1
        timeOut = datetime.datetime.time.now()

    class Meta:
        verbose_name_plural = ["PeopleOut"]


class Sensores(PeopleOut, PeopleIn):
    countIn = models.ForeignKey(CountIn, on_delete=models.CASCADE)
    countOut = models.ForeignKey(CountOut, on_delete=models.CASCADE)
    countNow = models.IntegerField(default=0)

    def calculateCant(countIn, countOut):
        cant = countIn.countIn - countOut.countOut
        return cant

    def calculateTime(countIn, countOut):
        a = a
        #Terminarrr

    class Meta:
        verbose_name_plural = ["PeoplesCount"]

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Localization(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignObject(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.city + ", " + self.country

class Store(models.Model):
    name = models.CharField(max_length=30, default="")
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE)
    maxCapability= models.IntegerField(default=0)

