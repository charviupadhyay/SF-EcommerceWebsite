from django.db import models

# Create your models here.
# import the standard Django Model
# from built-in library
from django.db import models
  
# declare a new model with a name "GeeksModel"
class Product(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    
class Hotel(models.Model):
     name = models.CharField(max_length=50)
     hotel_Main_Img = models.ImageField(upload_to='images/')