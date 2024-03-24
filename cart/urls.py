from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('viewcart/<int:user_id>', views.view_cart,name='viewcart'),
    path('order', views.order,name='order'),
]