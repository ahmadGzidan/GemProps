from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator
from GemProps import settings 

# Create your models here.
class House(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    prop_type=models.CharField(max_length=30)
    bedrooms=models.IntegerField(validators=[MinValueValidator(0)])
    bathrooms=models.IntegerField(validators=[MinValueValidator(0)])
    size=models.IntegerField(validators=[MinValueValidator(0)])
    available=models.DateField()
    description=models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    location=models.TextField()
    transaction_type= models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')


    def __str__(self):
        return self.prop_type
    class Meta:
        ordering=['available']


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey('House', on_delete=models.CASCADE) 
    def __str__(self):
        return house.prop_type

     
