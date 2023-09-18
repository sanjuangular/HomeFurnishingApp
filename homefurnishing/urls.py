from django.contrib import admin
from django.urls import path, include
from core.views import CustomLoginView  # Import the CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),  # Use CustomLoginView from imported views
    path('', include('core.urls')),
]
from django.contrib import admin
from django.urls import path, include
from core.views import CustomLoginView  # Import the CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),  # Use CustomLoginView from imported views
    path('', include('core.urls')),
]
