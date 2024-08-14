from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Customer, Purchase, PurchaseItem
from .forms import CategoryForm, ProductForm, PurchaseForm, CustomerForm
from django.contrib.auth.views import LoginView 
from django.contrib.auth.decorators import login_required
from datetime import date

#index
def index(request):
    return render(request, 'index.html')

# View para listar las categorías
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

# View para crear una nueva categoría
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza_menu:category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

# View para editar una categoría existente
@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES,instance=category)
        if form.is_valid():
            form.save()
            return redirect('pizza_menu:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

# View para eliminar una categoría
@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('pizza_menu:category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

# View para listar los productos
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# View para crear un nuevo producto
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza_menu:product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

# View para ver los detalles del producto
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# View para editar un producto existente
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('pizza_menu:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

# View para eliminar un producto
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('pizza_menu:product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

# View para listar las compras
def purchase_list(request):
    purchases = Purchase.objects.all().order_by('-date')
    return render(request, 'purchase_list.html', {'purchases': purchases})

# View para crear una nueva compra

def purchase_create(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            total = 0
            for product in form.cleaned_data['products']:
                total += product.price
            purchase.total = total
            purchase.save()
            form.save_m2m()  # Guardar relaciones Many-to-Many
            return redirect('pizza_menu:purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'purchase_form.html', {'form': form})

# View para ver detalles de una compra
def purchase_detail(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    return render(request, 'purchase_detail.html', {'purchase': purchase})

#View para listar a los clientes
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers':customers})

# View para agregar un nuevo cliente
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza_menu:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

# View para editar un cliente existente
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('pizza_menu:customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form})

# View para eliminar un cliente
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('pizza_menu:customer_list')
    return render(request, 'customer_confirm_delete.html', {'customer': customer})

class CustomLoginView(LoginView):
    template_name = "login.html"