from django.urls import path
from MyShop.views import home

urlpatterns = [
    path('', home , name='home'),
]
