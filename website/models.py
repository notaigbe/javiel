from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


# Product model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='detari/javiel/products/', default='detari/javiel/products/default.jpg')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='detari/javiel/service/', default='detari/javiel/service/default.jpg')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='detari/javiel/products/', default='detari/javiel/products/default.jpg')

    def __str__(self):
        return self.name


# CartItem model
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        return self.quantity * self.product.price


# Order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


# WishlistItem model
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} in {self.user.username}'s wishlist"


STATUS = ((0, 'DRAFT'), (1, 'PUBLISH'))
CATEGORY = (('clothing', 'Clothing'), ('makeup', 'Make-Up'), ('catering', 'Catering'))


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(choices=CATEGORY, max_length=8, default='fish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    post = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='detari/javiel/blog/', default='detari/javiel/blog/default.jpg')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    @property
    def comments(self):
        comments = Comment.objects.order_by('-created_on')[:5]
        return comments


class Comment(models.Model):
    article = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
