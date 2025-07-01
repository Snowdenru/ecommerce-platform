from rest_framework import serializers

from apps.products.models import Product
from apps.products.serializer import ProductSerializer
from apps.promotions.models import Discount, PromoCode


class DiscountSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )
    is_valid = serializers.BooleanField(read_only=True)

    class Meta:
        model = Discount
        fields = (
            "id",
            "product",
            "product_id",
            "percent",
            "start_date",
            "end_date",
            "is_active",
            "is_valid",
            "created_at",
        )
        read_only_fields = ("created_at",)


class PromoCodeSerializer(serializers.ModelSerializer):
    is_valid = serializers.BooleanField(read_only=True)

    class Meta:
        model = PromoCode
        fields = (
            "id",
            "code",
            "discount_percent",
            "is_active",
            "is_cumulative",
            "valid_until",
            "is_valid",
            "created_at",
        )
        read_only_fields = ("created_at",)
