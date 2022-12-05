from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название категории')

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название продукта')
    text = models.TextField(verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    caategory = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
