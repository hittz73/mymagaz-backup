from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=64)
    full_description = models.TextField('Полное описание')
    price = models.TextField('Цена')
    photo = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title