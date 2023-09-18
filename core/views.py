from django.shortcuts import render
from django.urls import reverse
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Category, Item, Order, CartItem
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddToCartForm
from .models import Category, Item, Order, CartItem




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or another page
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page

def dashboard(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    print(categories)  # Add this line to check categories
    return render(request, 'core/dashboard.html', {'categories': categories, 'items': items})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'core/category_list.html', {'categories': categories})

def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Item.objects.filter(category=category)  # Use 'category' field
    return render(request, 'core/category_items.html', {'category': category, 'items': items})



def item_page(request):
    items = Item.objects.all()
    return render(request, 'core/item_page.html', {'items': items})

def item_details(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = AddToCartForm()  # Initialize the form

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            # Logic to add the item to the cart goes here

    return render(request, 'core/item_details.html', {'item': item, 'user': request.user, 'form': form})

@login_required
def orders(request):
    # Fetch orders for the current user
    orders = Order.objects.filter(customer=request.user)
    print(orders)  # Add this line to check orders

    context = {
        'orders': orders,
    }

    return render(request, 'core/orders.html', context)


def ordered_items(request, order_id):
    # Retrieve the specific order
    order = get_object_or_404(Order, id=order_id)
    # Retrieve the ordered cart items for the order
    ordered_cart_items = CartItem.objects.filter(order=order)

    context = {
        'order': order,
        'ordered_cart_items': ordered_cart_items,
    }

    return render(request, 'core/ordered_items.html', context)

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    
    # Redirect to 'orders' if the cart is empty, otherwise, render the checkout page
    if cart_items:
        return render(request, 'core/checkout.html', {'cart_items': cart_items})
    else:
        return redirect('orders')  # Redirect to the 'orders' page if the cart is empty

def home(request):
    return render(request, 'core/homepage.html')

def item_details(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'core/item_details.html', {'item': item, 'user': request.user})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        quantity = form.cleaned_data['quantity']

        # Create a CartItem object and associate it with the user and item
        cart_item, created = CartItem.objects.get_or_create(
            customer=request.user,
            item=item,
            defaults={'quantity': quantity}
        )

        if not created:
            # If the item is already in the cart, update the quantity
            cart_item.quantity += quantity
            cart_item.save()

        return redirect('checkout')  # Redirect to the cart or checkout page

    return render(request, 'core/item_details.html', {'item': item, 'user': request.user, 'form': form})


def register(request):
    if request.method == 'POST':
        # Get user input data from the form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']
        
        # Create a new user
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        # Other user profile creation logic (if needed)
        
        return redirect('login')  # Redirect to the login page after successful registration
    
    return render(request, 'registration/registration.html')

class CustomLoginView(LoginView):
    template_name = 'core/login.html'

    def get_success_url(self):
        return reverse('dashboard')  # Redirect to the dashboard upon successful login

