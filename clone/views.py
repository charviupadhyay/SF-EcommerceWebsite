#views
# myapp/views.py
from cProfile import Profile
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,User,authenticate
from django.contrib.auth import login ,logout
from django.contrib import messages
from django.core.mail import send_mail
from clone import views
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

import stripe # type: ignore
from django.conf import settings
from clone.models import (
    BillingDetails, CartTotal, Product, Cart,CartItem, Order, TotalPrice
)
from django.views.generic import TemplateView
from .forms import ProductForm






def my_view(request):
    # Get the current user
    user = request.user

    # Get the profile associated with the current user
    user_profile = Profile.objects.get(user=user)

    # Pass the profile data to the template
    products = Product.objects.all()

    # Now you can access profile fields like bio
    print(user_profile.bio)

    # Pass both the user_profile and products variables to the template
    context = {'user_profile': user_profile, 'products': products}

    # Render the template with the context
    return render(request, 'profile.html', context)


def product_form(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    form = ProductForm()
    return render(request, 'product_form.html', {'form': form})
    

def home2(request):
 	return render(request,'home2.html')

def home3(request):
 	return render(request,'home3.html')


def shop(request):
 	return render(request,'shop.html')

# def features(request):
	# return render(request,'shoping-cart.html')

def blog(request):
    # product = Product.objects.get(id=product_id)
    # cart, created = Cart.objects.get_or_create(user=request.user)
    # cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    # if not created:
    #     cart_item.quantity += 1
    #     cart_item.save()
    # return redirect('product_list')
	return render(request,'blog.html')

def about(request):
	return render(request,'about.html')

def contact(request):
 	return render(request,'contact.html')

def myaccount(request):
	return render(request,'myaccount.html')


def orderplace(request):
 	return render(request,'orderplace.html')

def checkout(request):
 	return render(request,'checkout.html')

def SignupPage(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		email=request.POST.get('email')
		pass1=request.POST.get('password1')
		pass2=request.POST.get('password2')

		if pass1!=pass2:
			return HttpResponse("your password and conform password are not same")

		else:
			my_user=User.objects.create_user(uname,email,pass1)
			my_user.save()
			
			return redirect('login')

	return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')



def LogoutView(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


    # return render(request, 'index.html', data)


def shopingcart(request):
    products = Product.objects.all()
    return render(request, 'shopingcart.html', {'products': products})


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
    

# def product_list(request):
    # products = Product.objects.all()
    # return render(request, 'index.html', {'products': products})
# 
# def cart_view(request):
    # cart = Cart.objects.get(user=request.user)
    # return render(request,'cart.html',{'cart': cart})
# 
# 
# 
# 
# 
# 
# @login_required  # Ensure user is logged in
# def add_to_cart(request, product_id):
    # product = get_object_or_404(Product, id=product_id)
    # cart, created = Cart.objects.get_or_create(user=request.user)
    # cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
# 
    # if not cart_item_created:
        # cart_item.quantity += 1
        # cart_item.save()
    # else:
        # cart_item.quantity = 1
        # cart_item.save()
# 
    # Optionally, you can return data about the added item, such as its name, price, etc.
    # data = {
        # 'success': True,
        # 'message': 'Item added to cart successfully',
        # Add any additional data you want to return
    # }
# 
    # return JsonResponse(data)
# 
# payment add manually
# 
    stripe.api_key = settings.STRIPE_SECRET_KEY
# 
def payment_form(request, product_id):
     product = Product.objects.get(pk=product_id)
     publishable_key = settings.STRIPE_PUBLISHABLE_KEY
     return render(request, 'payment_form.html', {'product': product, 'publishable_key': publishable_key})
# 
# def charge(request, product_id):
    # if request.method == 'POST':
        # product = Product.objects.get(pk=product_id)
        # amount = int(product.price * 100)  # Amount in cents
        # token = request.POST['stripeToken']
        # charge = stripe.Charge.create(
            # amount=amount,
            # currency='usd',
            # description=product.name,
            # source=token
        # )
        # Create an order record after successful payment
        # Order.objects.create(
            # user=request.user,
            # product=product,
            # amount=product.price,
            # stripe_token=token
        # )
        # return redirect('payment_success')



# List all products
def product_list(request):
    products = Product.objects.all()
    return render(request,'index.html', {'products': products})

def deshboard(request):
    return render(request,'deshboard.html')
# View cart

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})
# quick_view
def quick_view(request):
    return render(request,'quick_view.html')

# Add product to cart
# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
#     if not cart_item_created:
#         cart_item.quantity += 1
#     else:
#         cart_item.quantity = 1
#     cart_item.save()

#     # Optionally, you can return data about the added item, such as its name,
#     data = {
#         'success': True,
#         'message': 'Item added to cart successfully',
#         # Add any additional data you want to return
#     }

    # return JsonResponse(data)

@require_POST
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    # Assuming you have a Cart model or session-based cart management
    cart = Cart.objects.get(user=request.user)  # Or however you manage the cart
    cart.add(product, quantity)
    
    return redirect('shop')

@require_POST
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Assuming you have a Cart model or session-based cart management
    cart = Cart.objects.get(user=request.user)  # Or however you manage the cart
    cart.remove(product)
    
    return redirect('shop')

# Payment form
def payment_form(request, product_id):
    product = Product.objects.get(pk=product_id)
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'payment_form.html', {'product': product, 'publishable_key': publishable_key})

# Charge user for the purchase
# def charge(request, product_id):
    # if request.method == 'POST':
        # product = Product.objects.get(pk=product_id)
        # amount = int(product.price * 100)  # Amount in cents
        # token = request.POST['stripeToken']
        # stripe.api_key = settings.STRIPE_SECRET_KEY
        # charge = stripe.Charge.create(
            # amount=amount,
            # currency='usd',
            # description=product.name,
            # source=token
        # )
        # Create an order record after successful payment
        # Order.objects.create(
            # user=request.user,
            # product=product,
            # amount=product.price,
            # stripe_token=token
        # )
        # return redirect('payment_success')


stripe.api_key = settings.STRIPE_SECRET_KEY

# Define a function-based view for the home page
def home1(request):
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'h1.html', context)

# Define a function-based view to handle the payment charge
def charge2(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=500,  # Amount in cents
                currency='inr',
                description='Payment Gateway',
                source=token
            )
            return render(request, 'charge2.html')
        except stripe.error.CardError as e:
            # Display error to user
            error_msg = e.error.message
            return render(request, 'error.html', {'error_msg': error_msg})
        except Exception as e:
            # Handle other exceptions
            return render(request, 'error.html', {'error_msg': str(e)})
    else:
        return render(request, 'error.html', {'error_msg': 'Invalid request method'})

def calculate_total(request):
    # Your logic to calculate total price
    total_price = 100  # For example

    # Save the total price to the database
    TotalPrice.objects.create(amount=total_price)

    # Return the total price as JSON response
    return JsonResponse({'total_price': total_price})

def create_billing_details(request):
    if request.method == 'POST':
        billing_details = BillingDetails(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            state_country=request.POST.get('state_country'),
            street_address=request.POST.get('street_address'),
            city=request.POST.get('city'),
            postcode=request.POST.get('postcode'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            create_account=request.POST.get('create_account') == 'on',
            ship_to_different_address=request.POST.get('ship_to_different_address') == 'on'
        )
        billing_details.save()
        # Optionally, you can redirect to another page upon successful creation
        return redirect('success_page')
    return render(request, 'checkout.html')

def create_cart_total(request):
    if request.method == 'POST':
        cart_total = CartTotal(
            subtotal=request.POST.get('subtotal'),
            delivery=request.POST.get('delivery'),
            discount=request.POST.get('discount'),
            total=request.POST.get('total')
        )
        cart_total.save()
        # Optionally, you can redirect to another page upon successful creation
        return redirect('success_page')
    return render(request, 'checkout.html')



def hotel_image_view(request):
 
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})
 

def search(request):
    query = request.GET.get('search')
    results = None
    if query:
        # Perform the case-insensitive search matching partially on the 'name' field of your Product model
        results = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})

def search_results(request):
    return render(request, 'search_results.html')