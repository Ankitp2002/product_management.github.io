from django.contrib import admin
from .models import Product,Signup,Blog,Entry,Author, Product_view, oContact, vprofile
from pyexpat import model
# Register your models here.
class padmin(admin.ModelAdmin):
    list_display = ['name','email','numbers']
    list_filter = ['name','email','numbers']
admin.site.register(Product,padmin)

class signupadmin(admin.ModelAdmin):
    list_display = ['name','email','mobile_no']
    list_filter = ['name','email','mobile_no']
admin.site.register(Signup,signupadmin)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)

class productadmin(admin.ModelAdmin):
    list_display = ['name','dec','price','rating']
    list_filter = ['name','dec','price','rating']
admin.site.register(Product_view,productadmin)
# class REG(admin.ModelAdmin):
#     list_display: ['name','dec','price','rating']

# admin.site.register(Register,REG)
class vadmin(admin.ModelAdmin):
    list_display = ['name' , 'm_no', 'bussiness_type']
    list_filter = ['name' , 'm_no' , 'bussiness_type']
admin.site.register(vprofile,vadmin)
admin.site.register(oContact)
