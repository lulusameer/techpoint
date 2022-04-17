# Generated by Django 3.2.12 on 2022-04-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category_pics/default.jpg', upload_to='category_pics/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product_pics/default.jpg', upload_to='product_pics/'),
        ),
    ]