from django.db import models
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30, null=False)
    sizes = models.ManyToManyField(Category, related_name='products')#Relación de muchos a muchos con la tabla categorías
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.CharField(max_length=400, null=False)

    def __str__(self):
        return self.name

#Creo la tabla Clientes
class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
#Creo la tabla Compras
class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Purchase {self.customer.first_name}"
    
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

