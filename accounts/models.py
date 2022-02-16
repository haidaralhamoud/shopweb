from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "proImage/%s.%s"%(instance.id,extension)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    image = models.ImageField(upload_to=image_upload,default='photo.jpg')
    def __str__(self):
        return str(self.user)

    
## create new user ---> create new empty profile

@receiver(post_save, sender=User)
def create_user_profile(sender,instance, created ,**kwargs):
    if created:
        Employee.objects.create(user=instance)
    

