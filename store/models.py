from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creater')
    name = models.CharField(max_length=100, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    in_stock = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    profession = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Reviews'
        
    def __str__(self):
        return self.name



class Subscription(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Subscriptions'
        
    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user/wishlist')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()