from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from cart.models import Cart, Order

def view_cart(request, user_id):
    user = request.user
    userprofile, created = user.objects.get_or_create(user=user)
    cart, created = cart.objects.get_or_create(user=user)
    all_products = cart.product.all()
    return render(request, 'cart/viewcart.html', {'products': all_products,
                                                   'totalPrice': cart.get_total_price(),
                                                   'user': user})

def order(request):
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        cart = get_object_or_404(Cart, user=request.user)
        order.product.set(cart.product.all())
        order.shipping_address = request.POST.get('shipping_address', '')
        order.zip_code = request.POST.get('zip_code', '')
        order.shipping_city = request.POST.get('shipping_city', '')
        order.shipping_district = request.POST.get('shipping_district', '')
        order.shipping_division = request.POST.get('shipping_division', '')
        order.phone_number = request.POST.get('phone_number', '')
        order.email = request.user.email
        order.save()
        cart.product.clear()
        return render(request, 'cart/orderConfirmed.html', {'order': order})
    else:
        cart = get_object_or_404(Cart, user=request.user)
        return render(request, 'cart/order.html', {'cart': cart,
                                                    'all_products': cart.product.all(),
                                                    'totalPrice': cart.get_total_price()})
