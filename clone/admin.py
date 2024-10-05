#admin.py
from django.contrib import admin
from clone.models import Category, Product,Cart,CartItem,Order,OrderItem, Sub_Category,TotalPrice,CartTotal,BillingDetails


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
  
admin.site.register(Category, CategoryAdmin)

class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
  
admin.site.register(Sub_Category, Sub_CategoryAdmin)










class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
  
admin.site.register(Product, ProductAdmin)

class CartItemInline(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ['id', 'user','sub_total']  # Display these fields in the admin list view
  
admin.site.register(Cart, CartAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'user', 'total_amount']  # Display these fields in the admin list view
  
admin.site.register(Order, OrderAdmin)


class TotalPriceAdmin(admin.ModelAdmin):
    list_display = ['amount']
  
admin.site.register(TotalPrice, TotalPriceAdmin)
# class ShippingInfoAdmin(admin.ModelAdmin):
    # list_display = ['user', 'country','state','street_address','apartment','city','postcode','phone','email']
#   
# admin.site.register(ShippingInfo, ShippingInfoAdmin)



class CartTotalAdmin(admin.ModelAdmin):
    list_display = ['subtotal', 'delivery','discount','total']
  
admin.site.register(CartTotal, CartTotalAdmin)


class BillingDetailsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','state_country','street_address','apartment_suite','city','postcode','phone','email','create_account','ship_to_different_address']
  
admin.site.register(BillingDetails, BillingDetailsAdmin)