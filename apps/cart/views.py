from rest_framework import generics, permissions, status

from .models import Cart, CartItem
from .serializer import CartItemSerializer, CartSerializer


class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serialize):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serialize.save(cart=cart)


class CartItemUpdateDestroyView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
