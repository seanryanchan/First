from django.contrib import admin

# Register your models here.
from Write_ups.models import Write_up
from Products.models import Product

admin.site.register(Write_up)
admin.site.register(Product)
