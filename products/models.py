from django.db import models
from djongo import models

# Create your models here.

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "proImage/%s.%s"%(instance,extension)

class Products(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    description2 = models.TextField(max_length=1000, blank=True, null=True )
    image = models.ImageField(upload_to=image_upload)
    hide = models.BooleanField(default=False)
    def __str__(self):
        return self.title


# class ArrayField(MongoField):
#         def __init__(self,
#                     model_container: typing.Type[Model],
#                     model_form_class: typing.Type[forms.ModelForm] = None,
#                     model_form_kwargs: dict = None,
#                     *args, **kwargs):
