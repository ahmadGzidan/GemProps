from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('offers/', include('offers.urls')),  # Include the accounts app's URLs
]
