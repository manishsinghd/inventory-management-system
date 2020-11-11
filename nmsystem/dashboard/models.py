from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="df.jpg",null=True, blank=True)
    shop_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self.name)


class Categorietype(models.Model):
    title = models.CharField(max_length=120)
    ACTIVE = 'active'
    INACTIVE = 'inactive'

    MY_CHOICES = [
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive')

    ]
    status_choice = models.CharField(max_length=8, choices=MY_CHOICES,
                                     default=INACTIVE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(models.Model):
    Brand = models.CharField(max_length=220)
    Model = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    description = models.TextField()
    Available = 'available'
    Unavailable = 'unavailable'

    CHOICES_MY = [
        (Available, 'available'),
        (Unavailable, 'unavailable')

    ]
    status = models.CharField(max_length=20, choices=CHOICES_MY)
    categorietype = models.ForeignKey(Categorietype, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Brand
# def create_profile(sender,instance,created,**kwargs):
# if created:
