from rest_framework import serializers 
from .models import House,Favorite


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=House
        fields ="__all__"


class HouseSerializer2(serializers.ModelSerializer):
    class Meta:
        model=House
        fields = ['prop_type', 'bedrooms', 'bathrooms', 'size', 'available', 'description', 'price', 'location', 'transaction_type','image','image1','image2']
    
    def get_is_favorite(self, obj):
        user = self.context['request'].user
        return Favorite.objects.filter(user=user, house=obj).exists()
        
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class HouseWithFavoriteSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = '__all__'

    def get_is_favorite(self, obj):
        user = self.context['request'].user
        return Favorite.objects.filter(user=user, house=obj).exists()
