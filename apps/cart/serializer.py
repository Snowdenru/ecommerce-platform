from rest_framework import serializers

from apps.products.models import Product
from apps.products.serializer import ProductSerializer

from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = (
            "id",
            "product",
            "product_id",
            "quantity",
            "total_price",
            "created_at",
        )
        read_only_fields = ("created_at",)

    def get_total_price(self, obj):
        return obj.total_price


class CartSerializer(serializers.ModelSerializer):

    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ("id", "user", "items", "total_price", "created_at")
        read_only_fields = (
            "user",
            "created_at",
        )

    def get_total_price(self, obj):
        return obj.total_price
