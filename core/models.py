from django.db import models
from django.contrib.auth.models import User

from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images', default='category_images/bed_sets.jpg')
    overlay_image = models.ImageField(upload_to='category_images', default='category_images/overlay_bedroom.png')




class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="No description available")
    image = models.ImageField(upload_to='static/item_images', default='item_images/king_bed.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, null=True, blank=True)  # Add Color field
    sizes = models.CharField(max_length=100, null=True, blank=True)  # Add Sizes field
    rate_3_months = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Add Rate for 3 months field


class Order(models.Model):
    STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ordered')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
