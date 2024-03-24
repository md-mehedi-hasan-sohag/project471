from pyexpat import model
from django.db import models
from testing.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    def get_total_price(self):
        total_price = 0
        for p in self.product.all():
            total_price += p.price
        return total_price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    shipping_address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    shipping_city = models.CharField(max_length=200)
    shipping_district = models.CharField(max_length=200)
    shipping_division = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    def get_total_price(self):
        total_price = 0
        for p in self.product.all():
            total_price += p.price
        return total_price