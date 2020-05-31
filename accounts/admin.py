from django.contrib import admin
from .models import Customers, Products, Order, Tag

# Register your models here.
admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Tag)