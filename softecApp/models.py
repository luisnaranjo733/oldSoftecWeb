from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant, null=True)

    def __str__(self):
        return '%s (%s)' % (self.user.username.capitalize(), self.restaurant.name.capitalize())

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Order: (%s, %s)>' % (self.pk, self.customer.user.username)

class Product(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return '<OrderProduct>'