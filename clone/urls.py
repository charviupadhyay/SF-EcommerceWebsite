"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[
    path('',views.index,name='index'),
    path('home2/',views.home2,name='home2'),
    path('home3/',views.home3,name='home3'),
    path('shop/',views.shop,name='shop'),
    # path('features/',views.features,name='features'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
    path('myaccount/',views.myaccount,name='myaccount'),

    path('contact/',views.contact,name='contact'),
    path('orderplace/',views.orderplace,name='orderplace'),
    path('checkout/',views.checkout,name='checkout'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('logout/',views.LogoutView, name='logout'),  # Add this line for logout'),
    path('shopingcart/',views.shopingcart, name='shopingcart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),    path('cart/',views.cart_view, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    #reset password
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='/home/psitint/Desktop/amazon/amazon/templates/password_reset_done.html'),name='password_reset_complete'),
    # manually added sign up with google
    path('social-auth/',include('social_django.urls',namespace='social')),

    #payment
    # path('charge/',views.charge, name='charge'),
    path('payment_form/',views.payment_form, name='payment_form'),
    path('charge2/',views.charge2,name='charge2'),
    path('home1/',views.home1,name='home1'),
    path('calculate-total/', views.calculate_total, name='calculate_total'),
    path('create-billing-details/',views.create_billing_details, name='create_billing_details'),
    path('image_upload', views.hotel_image_view, name='image_upload'),
    # path('success', views.success, name='success'),
    path('quick_view/',views.quick_view,name='quick_view'),
    path('product/', views.product_form, name='product_form'),
    path('deshboard/',views.deshboard,name='deshboard'),
    path('search/',views.search,name='search'),
    path('search_results/',views.search_results,name='search_results'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
