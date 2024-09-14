from django.contrib import admin

from website.models import Product, CartItem, WishlistItem

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(WishlistItem)
