from django.contrib import admin
from .models import Order, OrderItem, Coupon


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'status', 'total', 'payment_method', 'created_at']
    list_filter = ['status', 'payment_method', 'created_at']
    list_editable = ['status']
    search_fields = ['order_number', 'user__username', 'email']
    readonly_fields = ['order_number', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
    fieldsets = (
        ('Order Info', {'fields': ('order_number', 'user', 'status', 'payment_method', 'coupon')}),
        ('Customer Details', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Shipping Address', {'fields': ('address', 'city', 'postcode', 'country')}),
        ('Pricing', {'fields': ('subtotal', 'discount_amount', 'shipping_cost', 'total')}),
        ('Notes', {'fields': ('notes',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_percent', 'used_count', 'max_uses', 'active', 'valid_from', 'valid_to']
    list_editable = ['active']
    search_fields = ['code']
