

from django.urls import path
from .views import proview,Signupform,contact,vanderprofile,home,loginview,add_product,Searchview,prodelete,logout, vprofileview,service,owContact

urlpatterns = [
    path('proview/<int:abc>/',proview,name='proview'), 
    path('del/<int:abc>/',prodelete,name='prodel'), 
    path('signup/',Signupform,name='Signup'),
    path('contact/',contact,name='contact'),
    # path('productall/',productall,name='proall'),
    path('main/',home,name='home'),
    path('',loginview,name='loginview'),
    path('search/',Searchview,name='search'),
    path('add_product/',add_product,name='add_product'),
    path('vprofile/',vanderprofile,name='vanderprofile'),
    path('logout/',logout,name='logout'),
    path('vcp/',vprofileview,name='vcp'),
    path('service/',service,name='service'),
    path('owenerContact/',owContact,name='oContact')
]
