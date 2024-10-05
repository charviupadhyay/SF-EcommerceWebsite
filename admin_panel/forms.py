# from clone.models import Product
# from django import forms


# class ProductForm(forms.ModelForm):

#     class Meta:
#         model = Product
#         fields = '__all__'

from django import forms
from .models import Hotel
 
 
class HotelForm(forms.ModelForm):
 
    class Meta:
        model = Hotel
        fields = ['name', 'product-07.jpg']


