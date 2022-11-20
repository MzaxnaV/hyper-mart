from django.contrib import admin

from .models import Product, Brand

# Register your models here.

admin.site.register(Brand)
admin.site.register(Product)
