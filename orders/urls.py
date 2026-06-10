from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),
    path('remove-coupon/', views.remove_coupon, name='remove_coupon'),
    path('confirm/<str:order_number>/', views.order_confirm, name='order_confirm'),
    path('history/', views.order_history, name='order_history'),
    path('<str:order_number>/', views.order_detail, name='order_detail'),
]
