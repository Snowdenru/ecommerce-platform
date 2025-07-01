from django.db import models
from django.utils import timezone
from apps.products.models import Product


class Discount(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='discounts'
    )
    percent = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField( default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'discount'
        verbose_name_plural = 'discounts'

    def __str__(self):
        return f'{self.percent}% off {self.product.name}'

    @property
    def is_valid(self):
        now = timezone.now()
        return self.is_active and self.start_date <= now <= self.end_date

class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_cumulative = models.BooleanField(
        default=False,
        help_text='Can be used with other discounts'
    )
    valid_until = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'promo code'
        verbose_name_plural = 'promo codes'

    def __str__(self):
        return self.code

    @property
    def is_valid(self):
        now = timezone.now()
        return self.is_active and now <= self.valid_until