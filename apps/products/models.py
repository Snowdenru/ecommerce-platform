from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('Запас')
    image = models.ImageField('Изображение', upload_to='products/', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name