from django.db import models
from products.models import Products
from django.contrib.auth.models import User

# from django.contrib.postgres.fields import ArrayField

# # Create your models here.
def all_products():
    product = Products.objects.all()
    return product

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "proImage/%s.%s"%(instance.id,extension)

class Order(models.Model):
    user = models.CharField(max_length=50,default='admin')

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now=True)
    id_products = models.IntegerField(default=4)
    products = models.ManyToManyField(Products,blank=True,null=True,default=all_products)
    quantity = models.IntegerField(default=1)
    receive = models.IntegerField(default=1)
    done = models.IntegerField(default=2)
    image = models.ImageField(upload_to=image_upload,default='photo.jpg')
    locx = models.FloatField()
    locy = models.FloatField()

    # location = models.ManyToManyField(Location)
    def __str__(self):
        return self.name
# class Odder_details(models.Model):
#     pass