from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    override = request.POST.get('override', 'false') == 'true'
    cart.add(product=product, quantity=quantity, override_quantity=override)
    messages.success(request, f'"{product.name}" added to your cart!')
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'cart_count': len(cart), 'total': str(cart.get_total_price())})
    return redirect('cart_detail')


@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, f'"{product.name}" removed from cart.')
    return redirect('cart_detail')


@require_POST
def update_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart.add(product=product, quantity=quantity, override_quantity=True)
    else:
        cart.remove(product)
    return redirect('cart_detail')
