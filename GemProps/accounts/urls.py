from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Other URL patterns for the 'accounts' app
    path('registration/', views.registration_view, name='registration'),
    path('login/', obtain_auth_token, name="login"),
    path('logout/', views.logout, name='logout'),
]
