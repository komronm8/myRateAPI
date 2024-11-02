from django.urls import path
from .views import get_addresses, create_address, address_detail

urlpatterns = [ 
    path('address/all', get_addresses, name='get_addresses'),
    path('address/', create_address, name='create_address'),
    path('address/<int:pk>', address_detail, name='address_detail')
]
