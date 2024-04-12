from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id= _cart_id(request)
        )

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )

    return redirect('cart')


def cart(request):
    cart = Cart.objects.filter(cart_id=_cart_id(request))
    cart_items = CartItem.objects.all().filter(cart=cart[:1])
    return render(request, 'store/cart.html', {'cart': cart, 'cart_items': cart_items})
