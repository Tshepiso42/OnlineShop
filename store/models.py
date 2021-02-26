from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)



class Address(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=30)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return "oh yeah"

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length = 250, blank=True)
    additional_info = models.CharField(max_length = 250, blank=True)
    image = models.ImageField(upload_to = 'images')
    extra_img1 = models.ImageField(upload_to='images', default='Default Value')
    extra_img2 = models.ImageField(upload_to='images', default='Default Value')
    extra_img3 = models.ImageField(upload_to='images', default='Default Value')

    def __str__(self):
        return self.product_name


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)



