from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product, name='product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]