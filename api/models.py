from django.db import models

# Create your models here.

# def image_upload(instance,filename):
#     imagename , extension = filename.split(".")
#     return "proImage/%s.%s"%(instance.id,extension)

# class Products(models.Model):
#     title = models.CharField(max_length=50)
#     price=models.IntegerField()
#     description = models.TextField(max_length=1000)
#     image = models.ImageField(upload_to=image_upload)

#     def __str__(self):
#         return self.title

