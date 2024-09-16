from django.contrib import admin

from website.models import Product, CartItem, WishlistItem, Blog, Project, Service

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(WishlistItem)
admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(Service)
