from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from today.models import Product
from .forms import AddProductForm
from .cart import Cart


@require_POST
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, is_update=cd['is_update'])
    return redirect('cart:cart_detail')


def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def detail(request):
    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'is_update':True})
    return render(request, 'cart/cart_detail.html', {'cart':cart})
