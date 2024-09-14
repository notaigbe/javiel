from django.urls import path
from .views import (
    HomeView, AboutView, ServicesView, BlogView, BlogDetailView,
    ProductView, ProductDetailView, CartView, CheckoutView,
    ContactView, WishlistView, WorksView, add_to_cart, remove_from_cart, add_to_wishlist, remove_from_wishlist
)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog-detail'),
    path('products/', ProductView.as_view(), name='product'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('works/', WorksView.as_view(), name='works'),
]
