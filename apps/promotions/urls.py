from django.urls import path
from .views import (
    DiscountListCreateView, DiscountRetrieveUpdateDestroyView,
    PromoCodeListCreateView, PromoCodeRetrieveUpdateDestroyView
)

urlpatterns = [
    path('discounts/', DiscountListCreateView.as_view(), name='discount-list'),
    path('discounts/<int:pk>/', DiscountRetrieveUpdateDestroyView.as_view(), name='discount-detail'),
    path('promocodes/', PromoCodeListCreateView.as_view(), name='promocode-list'),
    path('promocodes/<int:pk>/', PromoCodeRetrieveUpdateDestroyView.as_view(), name='promocode-detail'),
]