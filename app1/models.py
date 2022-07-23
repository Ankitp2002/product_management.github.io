
from distutils.command.upload import upload
from email.mime import image
from msilib.schema import Media
import numbers
from tkinter.tix import MAX
from urllib import request
from django.db import models


# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    numbers=models.IntegerField(default='')
    password=models.CharField(max_length=8 , default='')
    up=models.ForeignKey('signup',on_delete=models.CASCADE,null=True,blank=True)
   

class Signup(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    password=models.CharField(max_length=8)
    image=models.ImageField(upload_to='signup_image')
    address=models.TextField(max_length=50,default='')
    bussiness_type=models.CharField(max_length=50,default='')
    def __str__(self):
        return str(self.name)
  

    # def __str__(self):
    #     return str(self.mobile_no)



class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()



class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

 

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


class Product_view(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='product_view')
    dec = models.TextField(max_length=50)
    price = models.IntegerField(default='')
    rating = models.FloatField(default='')
    up=models.ForeignKey('Signup',on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return str(self.up)

class vprofile(models.Model):
    name = models.CharField(max_length=10)
    bussiness_type=models.CharField(max_length=20)
    email=models.EmailField(default='')
    m_no=models.IntegerField()
    address=models.TextField(max_length=50)
    image=models.ImageField(upload_to='vimage')
    up=models.ForeignKey('Signup',on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return str(self.up)
class oContact(models.Model):
    name = models.CharField(max_length=10)
    number = models.IntegerField()
    problem = models.CharField(max_length=300)
    bussiness_type = models.CharField(max_length=20)
    up=models.ForeignKey('Signup',on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return str(self.up)
    
  
