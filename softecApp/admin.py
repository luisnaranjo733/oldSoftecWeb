from django.contrib import admin

from .models import Staff, Restaurant, Customer, Order, Product, OrderProduct

models = [Staff, Restaurant, Customer, Order, Product, OrderProduct]
for model in models:
    admin.site.register(model)