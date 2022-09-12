from django.contrib import admin
from .models import Products
# Register your models here.

@admin.register(Products)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_product', 'quantity', 'condition', 'image_url', 'updated', 'created' )
    
