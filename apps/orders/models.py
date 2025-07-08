from django.db import models
from apps.accounts.models import User
from apps.products.models import Product
from apps.promotions.models import PromoCode
from django.conf import settings

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        SHIPPED = "shipped", "Shipped"
        DELIVERED = "delivered", "Delivered"
        CANCELLED = "cancelled", "Cancelled"

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="orders",
        verbose_name="Пользователь",
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        "Статус", max_length=20, choices=Status.choices, default=Status.PENDING
    )
    promo_code = models.ForeignKey(
        PromoCode, on_delete=models.SET_NULL, null=True, blank=True
    )
    cashback_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cashback_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.id} {self.user.email}"

    def save(self, *args, **kwargs):
        if self.status == self.Status.PAID and not self.cashback_earned:
            profile = self.user.profile
            cashback = self.total * settings.CASHBACK_PERCENT / 100
            self.cashback_earned = cashback
            profile.cashback_balance += cashback
            profile.save()
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='order_items',
    )
    quantity = models.PositiveIntegerField()
    price_at_order = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'order item'
        verbose_name_plural = 'order items'

    def __str__(self):
        return f'{self.quantity} x {self.product.name} at {self.price_at_order}'