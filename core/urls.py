from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('item-page/', views.item_page, name='item_page'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_items, name='category_items'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('item/<int:item_id>/', views.item_details, name='item_details'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('ordered_items/<int:order_id>/', views.ordered_items, name='ordered_items'),
    path('logout/', views.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)