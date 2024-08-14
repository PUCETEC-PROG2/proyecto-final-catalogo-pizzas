from django import forms
from .models import Category, Product, Purchase, Customer

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
        fields = ['name', 'sizes', 'price', 'ingredients']
        labels = {
            'name': 'Nombre del Producto',
            'sizes': 'Categorías',
            'price': 'Precio',
            'ingredients': 'Ingredientes',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sizes': forms.SelectMultiple(attrs={'class': 'form-control'}),  # Cambiado a SelectMultiple
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PurchaseForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Purchase
        fields = ['customer', 'date', 'products']

    def save(self, commit=True):
        purchase = super().save(commit=False)

        if commit:
            purchase.save()  # Guardar la instancia de Purchase
            self.save_m2m()  # Guardar las relaciones many-to-many después

        return purchase

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }