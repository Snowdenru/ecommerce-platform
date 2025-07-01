from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "stock", "image", "create_at")
        read_only_fields = ("create_at",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["image"] = instance.image.url if instance.image else None

        active_discount = instance.discounts.filter(is_active=True).first()
        if active_discount:
            representation["discount"] = {
                "percent": active_discount.percent,
                "discounted_price": instance.price
                * (100 - active_discount.percent)
                / 100,
            }
        return representation
