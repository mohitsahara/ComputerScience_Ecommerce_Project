from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from decimal import Decimal
from cart.cart import Cart
from .models import Order, OrderItem, Coupon
from .forms import CheckoutForm, CouponForm


@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart_detail')

    coupon_id = request.session.get('coupon_id')
    coupon = None
    discount_amount = Decimal('0')

    if coupon_id:
        try:
            coupon = Coupon.objects.get(id=coupon_id)
            if coupon.is_valid:
                discount_amount = cart.get_total_price() * Decimal(coupon.discount_percent) / 100
        except Coupon.DoesNotExist:
            pass

    subtotal = cart.get_total_price()
    shipping = Decimal('0') if subtotal >= 50 else Decimal('4.99')
    total = subtotal - discount_amount + shipping

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.subtotal = subtotal
            order.discount_amount = discount_amount
            order.shipping_cost = shipping
            order.total = total
            if coupon:
                order.coupon = coupon
                coupon.used_count += 1
                coupon.save()
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price'],
                )
                # Reduce stock
                product = item['product']
                product.stock -= item['quantity']
                product.save()

            cart.clear()
            if 'coupon_id' in request.session:
                del request.session['coupon_id']

            messages.success(request, f'Order #{order.order_number} placed successfully! Thank you for shopping with TechMart.')
            return redirect('order_confirm', order_number=order.order_number)
    else:
        profile = getattr(request.user, 'profile', None)
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        if profile:
            initial.update({
                'phone': profile.phone,
                'address': profile.address,
                'city': profile.city,
                'postcode': profile.postcode,
                'country': profile.country,
            })
        form = CheckoutForm(initial=initial)

    coupon_form = CouponForm()
    return render(request, 'orders/checkout.html', {
        'cart': cart,
        'form': form,
        'coupon_form': coupon_form,
        'coupon': coupon,
        'subtotal': subtotal,
        'discount_amount': discount_amount,
        'shipping': shipping,
        'total': total,
    })


def apply_coupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code'].upper()
            try:
                coupon = Coupon.objects.get(code=code)
                if coupon.is_valid:
                    request.session['coupon_id'] = coupon.id
                    messages.success(request, f'Coupon "{code}" applied! {coupon.discount_percent}% discount.')
                else:
                    messages.error(request, 'This coupon is expired or no longer valid.')
            except Coupon.DoesNotExist:
                messages.error(request, 'Invalid coupon code.')
    return redirect('checkout')


def remove_coupon(request):
    if 'coupon_id' in request.session:
        del request.session['coupon_id']
        messages.info(request, 'Coupon removed.')
    return redirect('checkout')


@login_required
def order_confirm(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'orders/order_confirm.html', {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def order_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
