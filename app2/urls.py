from django.urls import path
from .views import productview

urlpatterns = [
   path('p/',productview)
    
]