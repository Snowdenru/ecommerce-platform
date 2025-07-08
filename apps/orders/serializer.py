from rest_framework import serializers

from apps.products.serializer import ProductSerializer
from apps.promotions.models import PromoCode
from apps.promotions.serializer import PromoCodeSerializer

from .models import Order, OrderItem
from django.conf import settings


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ("id", "product", "quantity", "price_at_order", "created_at")


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    promo_code = PromoCodeSerializer(read_only=True)
    promo_code_id = serializers.PrimaryKeyRelatedField(
        queryset=PromoCode.objects.filter(is_active=True),
        source="promo_code",
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "items",
            "total",
            "status",
            "promo_code",
            "promo_code_id",
            "cashback_used",
            "cashback_earned",
            "create_at",
        )
        read_only_fields = ("user", "status", "cashback_earned", "create_at")


    def validate(self, data):
        user = self.context['request'].user
        data['user'] = user
        
        # Validate cashback usage
        cashback_used = data.get('cashback_used', 0)
        if cashback_used > 0:
            profile = user.profile
            if cashback_used > profile.cashback_balance:
                raise serializers.ValidationError(
                    {'cashback_used': 'Not enough cashback balance'}
                )
            if cashback_used < settings.MIN_CASHBACK_AMOUNT:
                raise serializers.ValidationError(
                    {'cashback_used': f'Minimum cashback amount is {settings.MIN_CASHBACK_AMOUNT}'}
                )
        
        return data