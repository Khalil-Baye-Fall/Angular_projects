from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Products(models.Model):
    status_product = [
        ('new', 'New'),
        ('used', 'Used'),
        ('not used', 'Not Fonctional' )
    ]
    name = models.CharField(max_length=150)
    type_product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    condition = models.CharField(max_length=10, choices=status_product)
    image_url = models.URLField(default="no image available")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.name
    
    
class ReservationProduct(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()
    time_use = models.IntegerField(default=2)
    reason = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    
    
class Pick_return(models.Model):
    pass



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    