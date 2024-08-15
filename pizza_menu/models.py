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
    products = models.ManyToManyField(Product, through='PurchaseItem')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def calculate_total(self):
        # Asegúrate de que el método calculate_total suma correctamente los precios de los productos
        purchase_items = self.purchaseitem_set.all()
        print(f"Purchase items: {purchase_items}")  # Debug
        total = sum(item.product.price for item in purchase_items)
        print(f"Calculated total: {total}")  # Debug
        self.total = total

    def save(self, *args, **kwargs):
        # Calcula el total antes de guardar la instancia
        self.calculate_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Purchase {self.customer.first_name}"
    
#Creo la tabla intermedia PurchaseItem
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)#La llave foránea con la relación de muchos a uno con Purchase
    product = models.ForeignKey(Product, on_delete=models.CASCADE)#La llave foránea con la relación de muchos a uno con Product

