from django.db import models
import datetime


class Item(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField(default=datetime.datetime.now())
    value = models.FloatField(max_length=100)
    to_date = models.DateField(default=datetime.datetime.now())
    prise = models.FloatField(max_length=100)
    provider = models.CharField(max_length=100)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField(default=datetime.time(second=0))
    items = models.ManyToManyField(Item, "Items")


class StaffFunc(models.Model):
    name = models.CharField(max_length=100)
    prise = models.FloatField(max_length=100)
    duties = models.TextField()
    requirements = models.TextField()


class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pass_data = models.CharField(max_length=100)
    func = models.ForeignKey(StaffFunc)


class Order(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    is_success = models.BooleanField(default=False)
