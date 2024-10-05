#models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

#extra added by today
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(null=False, upload_to='product')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    sub_total = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.email}'
    
    # def get_calculated_subtotal(self):
    



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields like shipping details, payment status, etc.


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class TotalPrice(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class BillingDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    state_country = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    apartment_suite = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    create_account = models.BooleanField(default=False)
    ship_to_different_address = models.BooleanField(default=False)

class CartTotal(models.Model):
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    delivery = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

