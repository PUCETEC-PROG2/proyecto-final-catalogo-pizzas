from django import forms
from .models import Category, Product, Purchase

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nombre de la Categoría',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'categories', 'price', 'ingredients']
        labels = {
            'name': 'Nombre del Producto',
            'categories': 'Categorías',
            'price': 'Precio',
            'ingredients': 'Ingredientes',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['customer', 'products']
        labels = {
            'customer': 'Cliente',
            'products': 'Productos',
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'products': forms.CheckboxSelectMultiple(),
        }
