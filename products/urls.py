from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/search/', views.search_view, name='search'),
    path('products/category/<slug:slug>/', views.category_products, name='category_products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/<slug:slug>/review/', views.add_review, name='add_review'),
    path('products/<slug:slug>/wishlist/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('info/', views.info_page, name='info_page'),
    path('contact/', views.contact_page, name='contact_page'),
]
