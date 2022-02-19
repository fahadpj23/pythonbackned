
from distutils.command.upload import upload
from django.db import models

 

# Create your models here.
class cover(models.Model):

   
    productid=models.CharField( max_length=255)
    name=models.CharField(max_length=255)
    color=models.CharField(max_length=100)
    price=models.FloatField()
    mrp=models.FloatField()
    warranty=models.CharField( max_length=100)
    image=models.ImageField(upload_to="")
    material=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    maxqty=models.IntegerField()
    brand=models.CharField(max_length=255)



class headset(models.Model):

   
    productid=models.CharField( max_length=255)
    name=models.CharField(max_length=255)
    color=models.CharField(max_length=100)
    price=models.FloatField()
    mrp=models.FloatField()
    warranty=models.CharField( max_length=100)
    image=models.ImageField(upload_to="")
    material=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    maxqty=models.IntegerField()
    brand=models.CharField(max_length=255)
    headsettype=models.CharField(max_length=255)
