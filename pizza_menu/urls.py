from django.urls import path

from . import views

app_name = 'pokedex'

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

    path('purchases/', views.purchase_list, name='product_list'),
    path('purchase/new/', views.purchase_create, name='product_create'),
    path('purchase/<int:pk>/', views.purchase_detail, name='purchase_detail'),
]

