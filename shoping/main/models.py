from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Название категории', unique=True)
    slug = models.SlugField(max_length=100, db_index=True,
                            unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("Category", kwargs={"pk": self.pk})
    


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название бренда')
    slug = models.SlugField(
        max_length=100, verbose_name='URL', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Названия бренда'
        verbose_name_plural = 'Названии брендов'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("Brand", kwargs={"pk": self.pk})
    

class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name='Цвет')
    slug = models.SlugField(max_length=100, db_index=True,
                            unique=True, verbose_name='URL')

    class Meta:
        ordering = ['name']
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("Color", kwargs={"pk": self.pk})
    

class Specifications(models.Model):
    title = models.CharField(max_length=60, verbose_name='Наименования')
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['title']
        verbose_name = 'Спецификая'
        verbose_name_plural = 'Спецификации'

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Наименнования продукта')  # Наименнования
    brand = models.ManyToManyField(Brand, verbose_name='Бренд')  # Бренд товара
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    short_description = models.TextField(
        max_length=500, verbose_name='Краткое Описание')  # Краткое описания
    description = models.TextField(
        max_length=3000, verbose_name='полное описания')  # Полное описания товара
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')  # Цена
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE)  # Категории товара
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Выбор цвета')  # Цвет товара
    avibiality = models.PositiveIntegerField(
        default=0, verbose_name='Количество товара в складе')
    specifications = models.ManyToManyField(
        Specifications)  # Технические характеристки

    sold = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name} {self.brand}'

    def get_absolute_url(self):
        return reverse("Product detail", kwargs={"pk": self.pk})
