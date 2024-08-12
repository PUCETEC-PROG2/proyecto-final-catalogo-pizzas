from django.db import models

#Creo la tabla categorias
class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

#Creo la tabla productos
class Product(models.Model):
    name = models.CharField(max_length=30, null=False)
    categories = models.ManyToManyField(Category, related_name='products')#Relación de muchos a muchos con la tabla categorías 
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
    customer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='purchases')#Relación de uno a muchos con la tabla Purchase 
    products = models.ManyToManyField(Product, through='PurchaseItem')#Relación de muchos a muchos con la tabla Productos, por la tabla intermedia PurchaseItem
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Purchase {self.id} by {self.customer}'
    
#Creo la tabla intermedia PurchaseItem
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)#La llave foránea con la relación de muchos a uno con Purchase
    product = models.ForeignKey(Product, on_delete=models.CASCADE)#La llave foránea con la relación de muchos a uno con Product





    


