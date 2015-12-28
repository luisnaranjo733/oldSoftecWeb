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
    customerID = models.ForeignKey(Customer)
    cestaurantID = models.ForeignKey(Restaurant)

    def __str__(self):
        return '<Customer_Restaurant>'

class SalesOrder(models.Model):
    customerID = models.ForeignKey(Customer)
    # sales invoice FK?
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<SalesOrder: (%s, %s)>' % (self.pk, self.customerID.userID.username)

class ProductInventory(models.Model):
    productID = models.OneToOneField('Product', related_name='productInventoryID')
    quantity = models.IntegerField()

    def __str__(self):
        return '<ProductInventory: %s (%d)>' % (self.productID.name, self.quantity)

class Product(models.Model):
    #  replaced with OneToOneField()
    #ProductInventoryID = models.ForeignKey(ProductInventory)
    name =  models.CharField(max_length=200, unique=True)
    purchasePrice = models.DecimalField(max_digits=6, decimal_places=2)
    salesPrice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '<Product: %s>' % self.name

    def get_absolute_url(self):
        return '/products/%d' % self.id

    def getVendor(self):
        associative_entry = Vendor_Product.objects.get(productID=self)
        if associative_entry:
            return associative_entry.vendorID

class SalesOrder_Product(models.Model):
    salesOrderID = models.ForeignKey(SalesOrder)
    productID = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return '<SalesOrder_Product>'

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '<Vendor: %s>' % self.name

class Vendor_Product(models.Model):
    vendorID = models.ForeignKey(Vendor)
    productID = models.ForeignKey(Product)

    def __str__(self):
        return '<Vendor_Product: %s>' % self.productID.name

class PurchaseOrder(models.Model):
    vendorID = models.ForeignKey(Vendor)
    # Purchase invoice FK?
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<PurchaseOrder: %d>' % self.pk

class PurchaseOrderInvoice(models.Model):
    purchaseOrderID = models.OneToOneField(PurchaseOrder, related_name='purchaseOrderInvoiceID')
    orderSubmittedDate = models.DateTimeField()
    orderPaidDate = models.DateTimeField()
    orderDueDate = models.DateField()

class PurchaseOrder_Product(models.Model):
    purchaseOrderID = models.ForeignKey(PurchaseOrder)
    productID = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return '<PurchaseOrder_Product>'




app_models = [
    Staff, Restaurant, Customer, Customer_Restaurant, SalesOrder, Product,
    ProductInventory, SalesOrder_Product, Vendor, Vendor_Product,
    PurchaseOrder, PurchaseOrderInvoice, PurchaseOrder_Product
]

'''
Stored procedures
* Submitting a PurchaseOrder
    - Increment all related product inventory
* Submitting a SalesOrder
    - Decrement all related product inventory
'''