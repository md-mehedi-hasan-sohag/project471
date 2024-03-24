from django.shortcuts import render,redirect
from testing.models import Product
from cart.models import *
from cart.views import view_cart


# Create your views here.

def product(request,product_id):
    one_product = Product.objects.get(id=product_id)
    return render(request, 'Product/product.html', {'product': one_product})

def add_to_cart(request,product_id):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)
    except:
        cart = Cart.objects.create(user=user)
    product = Product.objects.get(id=product_id)
    cart.add(product)
    cart.save()
    return redirect(view_cart,user_id=request.user.id)

def remove_from_cart(request,product_id):
    user = request.user
    cart = Cart.objects.get(user=user)
    product = Product.objects.get(id=product_id)
    cart.product.remove(product)
    cart.save()
    return redirect(view_cart,user_id=request.user.id)