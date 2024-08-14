from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryaAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass