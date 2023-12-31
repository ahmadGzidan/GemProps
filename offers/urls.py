from django.contrib import admin
from . import views
from django.urls import path,include
from .views import HouseList,HouseDetail,HouseCreate,HouseDelete,HouseUpdate,HomePageView,MyListings,FavoriteListCreateView,FavoriteDetailView,myfavorites
app_name='offers'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('houses/',HouseList.as_view(),name='HouseList'),
    path('myListings/',MyListings.as_view(),name='MyListings'),
    path('house/<int:pk>/',HouseDetail.as_view(),name='HouseDetail'),
    path('house-create/',HouseCreate.as_view(),name='HouseCreate'),
    path('house-delete/<int:pk>/',HouseDelete.as_view(),name='HouseDelete'),
    path('house-update/<int:pk>/',HouseUpdate.as_view(),name='HouseUpdate'),
    path('<int:pk>/toggle_favorite/', views.ToggleFavoriteView.as_view(), name='toggle-favorite'),
    path('myfavorites/',myfavorites.as_view(),name='MyFavorites'),

]
