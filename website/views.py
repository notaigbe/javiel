from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem, Product, Order, WishlistItem, Blog


# from .models import Blog, Product  # Uncomment and modify based on your models

# Home view
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = "active"
        return context


# About view
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = "active"
        return context


# Services view
class ServicesView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = "active"
        return context


# Blog listing view
class BlogView(TemplateView):
    template_name = 'blog.html'

    # You can add context if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = "active"
        context['blogs'] = Blog.objects.all()
        return context


# Blog detail view
class BlogDetailView(DetailView):
    model = Blog  # Uncomment and modify based on your Blog model
    template_name = 'blog-details.html'

    context_object_name = 'blog_post'  # Name used in the template

    # If not using the model, you can manually get the object
    def get_object(self):
        blog_id = self.kwargs.get('id')
        # return get_object_or_404(Blog, id=blog_id)
        return {'id': blog_id}  # Example for context


# Product listing view
class ProductView(TemplateView):
    template_name = 'product.html'

    # Add context for product list if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = "active"
        return context


# Product detail view
class ProductDetailView(DetailView):
    # model = Product  # Uncomment and modify based on your Product model
    template_name = 'product-details.html'

    # context_object_name = 'product_item'

    def get_object(self):
        product_id = self.kwargs.get('id')
        # return get_object_or_404(Product, id=product_id)
        return {'id': product_id}  # Example for context


# Cart view
class CartView(TemplateView):
    template_name = 'cart.html'


# Checkout view
class CheckoutView(TemplateView):
    template_name = 'checkout.html'


# Contact view
class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = "active"
        return context


# Wishlist view
class WishlistView(TemplateView):
    template_name = 'wishlist.html'


# Works view
class WorksView(TemplateView):
    template_name = 'works.html'


# Shopping Cart view
@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'cart_total': cart_total})


# Add to Cart view
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=product, defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


# Remove from Cart view
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')


# Checkout view
@login_required
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == "POST" and cart_items.exists():
        order = Order.objects.create(user=request.user)
        total_price = sum(item.get_total_price() for item in cart_items)
        order.items.set(cart_items)
        order.total_price = total_price
        order.save()

        # Clear the cart after checkout
        cart_items.delete()

        # Redirect to a confirmation page or a payment gateway
        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'checkout.html', {'cart_items': cart_items})


# Wishlist view
@login_required
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


# Add to Wishlist view
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')


# Remove from Wishlist view
@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id, user=request.user)
    wishlist_item.delete()
    return redirect('wishlist')
