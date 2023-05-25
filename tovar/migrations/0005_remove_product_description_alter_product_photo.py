# Generated by Django 4.1.5 on 2023-05-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tovar', '0004_rename_image_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
