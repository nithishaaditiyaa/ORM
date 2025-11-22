from django.db import models
from django.contrib import admin
class ecommerce(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=20)
    manufracture_name=models.CharField(max_length=15)
    cost=models.IntegerField()
    company=models.CharField(max_length=15)
    email=models.EmailField()

class ecommerceAdmin(admin.ModelAdmin):
    list_display=["product_id" , "product_name" , "manufracture_name" , "cost" , "company" , "email"]