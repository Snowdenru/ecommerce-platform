from django.urls import path 
from .views import CartItemCreateView, CartView, CartItemUpdateDestroyView


urlpatterns = [

    path('', CartView.as_view(), name='cart'),
    path('items/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('items/<int:pk>', CartItemUpdateDestroyView.as_view(), name='cart-item-update-destroy'),

]
