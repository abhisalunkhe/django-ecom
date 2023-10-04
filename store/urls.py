from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('subscription',views.subscription,name='subscription'),
    path('account/<str:username>/', views.account, name='account'),
    path('account/<str:username>/logout', views.logout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('products',views.products,name='products'),
    path('wishlist/<str:username>/', views.wishlist, name='wishlist'),
    path('wishlist/<str:username>/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]