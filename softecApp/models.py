from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    userID = models.ForeignKey(User)

    def __str__(self):
        return self.userID.username


class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Customer(models.Model):
    userID = models.ForeignKey(User)
    restaurantID = models.ForeignKey(Restaurant, null=True)

    def __str__(self):
        return '%s (%s)' % (self.userID.username.capitalize(), self.restaurantID.name.capitalize())

class Customer_Restaurant(models.Model):
    CustomerID = models.ForeignKey(Customer)
    RestaurantID = models.ForeignKey(Restaurant)

    def __str__(self):
        return '<Customer_Restaurant>'

class SalesOrder(models.Model):
    customerID = models.ForeignKey(Customer)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<SalesOrder: (%s, %s)>' % (self.pk, self.customerID.userID.username)

class Product(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProductInventory(models.Model):
    productID = models.ForeignKey(Product)

    def __str__(self):
        return self.name

class SalesOrder_Product(models.Model):
    salesOrderID = models.ForeignKey(SalesOrder)
    productID = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return '<OrderProduct>'

app_models = [
    Staff, Restaurant, Customer, Customer_Restaurant, SalesOrder, Product,
    ProductInventory, SalesOrder_Product
]