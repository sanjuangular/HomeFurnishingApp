# custom_filters.py

from django import template

register = template.Library()

@register.filter
def calculate_total_price(cart_item):
    return cart_item.item.price * cart_item.quantity
