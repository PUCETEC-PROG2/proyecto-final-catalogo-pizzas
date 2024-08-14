from django.urls import path
from . import views

app_name = 'pizza_menu'

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/', views.category_list, name='category_list'),
    path('category/new/', views.category_create, name='category_create'),
    path('category/<int:pk>/edit/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    path('products/', views.product_list, name='product_list'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:pk>/detail/', views.product_detail, name='product_detail'),

    path('purchases/', views.purchase_list, name='purchase_list'),
    path('purchase/new/', views.purchase_create, name='purchase_create'),
    path('<int:purchase_id>/', views.purchase_detail, name='purchase_detail'),

    path('customers/', views.customer_list, name='customer_list'),
    path('customer/new/', views.customer_create, name='customer_create'),
    path('customer/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    path("login/", views.CustomLoginView.as_view(), name="login"),
]


