from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    products = Product.objects.all()
    reviews = Review.objects.all()
    context = {
        'products': products,
        'reviews': reviews
    }
    return render(request,'index.html',context)


def register(request):
    if request.method == "POST":
        if User.objects.filter(username = request.POST['fname']).exists():
            print("User Already Exists")
        elif User.objects.filter(email = request.POST['email']).exists():
            print("Email Already Existed")
        else:
            u = User.objects.create_user(username = request.POST['fname'],last_name = request.POST['lname'],email = request.POST['email'],password = request.POST['password'])
            u.save()
            return redirect('login')
    else:
        return render(request,'login.html')
    
def login(request):
    if request.method == "POST":
        user = auth.authenticate(username = request.POST['fname'],password = request.POST['password'])
        
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            print('Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')


def subscription(request):
    if request.method == 'POST':
        data = Subscription.objects.create(email = request.POST['email'])
        data.save()
        return redirect('/')
    else:
        return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')


@login_required
def account(request, username):
    if request.user.is_authenticated and request.user.username == username:
        user = request.user
        context = {
            'first_name': user.username,
            'last_name': user.last_name,
            'email': user.email,
        }
        return render(request, 'my-account.html', context)
    else:
        return redirect('login')

def contact(request):
    if request.method == 'POST':
        data = Contact.objects.create(name = request.POST['name'], email = request.POST['email'], subject = request.POST['subject'], message = request.POST['message'])
        data.save()
        return redirect('index')
    else:
        return render(request,'contact.html')

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'product-list.html',context)

@login_required
def wishlist(request, username):
    wishlist_items = Wishlist.objects.filter(user__username=username)
    
    context = {
        'wishlist_items': wishlist_items
    }
    
    return render(request, 'wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        Wishlist.objects.get_or_create(user=request.user, image = product.image, name = product.name, price = product.price, quantity = 1)
    return redirect('wishlist', username=request.user.username)


@login_required
def remove_from_wishlist(request, username, product_id):
    if request.user.is_authenticated:
        wishlist_item = get_object_or_404(Wishlist, user__username=username, id=product_id)
        wishlist_item.delete()
        print("Item deleted")
    else:
        print("User not authenticated")
    return redirect('wishlist', username=request.user.username)


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_image = request.POST.get('product_image')
        quantity = request.POST.get('quantity')

        cart = request.session.get('cart', {})
        cart[product_id] = {
            'name': product_name,
            'price': float(product_price),
            'image': product_image,
            'quantity': int(quantity),
        }
        request.session['cart'] = cart
    return redirect('wishlist', username=request.user.username)


@login_required
def cart(request):
    cart = request.session.get('cart', {})
    for item in cart.values():
        item['total_price'] = item['quantity'] * item['price']
    context = {'cart': cart}
    return render(request, 'cart.html', context)

def product_detail(request, product_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product, 'products':products}
    return render(request, 'product-detail.html', context)