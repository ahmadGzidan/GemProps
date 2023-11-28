from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import Account
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import House
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import HouseSerializer,HouseSerializer2,HouseWithFavoriteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Favorite
from .serializers import FavoriteSerializer
from rest_framework import generics


@permission_classes([IsAuthenticated])
class HouseList(ListAPIView,LoginRequiredMixin):
    serializer_class = HouseSerializer
    queryset = House.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

@permission_classes([IsAuthenticated])
class HouseDetail(RetrieveAPIView,LoginRequiredMixin):

    lookup_field = 'pk'
    serializer_class = HouseSerializer
    queryset = House.objects.all()

@permission_classes([IsAuthenticated])
class HouseCreate(CreateAPIView,LoginRequiredMixin):

    serializer_class = HouseSerializer2

    def perform_create(self, serializer):
        # Set the user field to the authenticated user
        serializer.save(user=self.request.user)

@permission_classes([IsAuthenticated])
class HouseUpdate(UpdateAPIView,LoginRequiredMixin):
    queryset = House.objects.all()
    serializer_class = HouseSerializer2
    lookup_field = 'pk'

@permission_classes([IsAuthenticated])
class HouseDelete(DestroyAPIView,LoginRequiredMixin):
    queryset = House.objects.all()
    lookup_field = 'pk'

@permission_classes([IsAuthenticated])
@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView,LoginRequiredMixin):
    template_name = 'offers/home.html'

@permission_classes([IsAuthenticated])
class MyListings(ListAPIView):
    serializer_class = HouseSerializer
    def get_queryset(self):
        return House.objects.filter(user=self.request.user)


@permission_classes([IsAuthenticated])
class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteDetailView(generics.RetrieveDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class ToggleFavoriteView(generics.UpdateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def put(self, request, *args, **kwargs):
        house = self.get_object()
        user = request.user

        # Check if the user has already favorited the house
        if Favorite.objects.filter(user=user, house=house).exists():
            # If the favorite exists, remove it
            Favorite.objects.filter(user=user, house=house).delete()
            return Response({'detail': 'Removed from favorites'}, status=status.HTTP_200_OK)
        else:
            # If the favorite does not exist, add it
            Favorite.objects.create(user=user, house=house)
            return Response({'detail': 'Added to favorites'}, status=status.HTTP_201_CREATED)


class myfavorites(generics.ListAPIView):
    serializer_class = HouseWithFavoriteSerializer

    def get_queryset(self):
        user = self.request.user
        favorites = Favorite.objects.filter(user=user)
        house_ids = favorites.values_list('house_id', flat=True)
        return House.objects.filter(id__in=house_ids)