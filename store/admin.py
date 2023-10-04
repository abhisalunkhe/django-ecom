from django.contrib import admin
from .models import *

# Register your models here.

class admin_category(admin.ModelAdmin):
    list_display = ['id', 'name']

class admin_product(admin.ModelAdmin):
    list_display = ['id','created_by', 'name', 'category', 'in_stock']

class admin_review(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession', 'created']

class admin_subscription(admin.ModelAdmin):
    list_display = ['id', 'email', 'created']

class admin_contact(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']

class admin_wishlist(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'price', 'quantity']


admin.site.register(Category, admin_category)
admin.site.register(Product, admin_product)
admin.site.register(Review, admin_review)
admin.site.register(Subscription, admin_subscription)
admin.site.register(Contact, admin_contact)
admin.site.register(Wishlist, admin_wishlist)