# Generated by Django 3.1 on 2020-09-05 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_categories_categoriesiconimage'),
        ('products', '0006_product_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='categories.categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(null=True, upload_to='product'),
        ),
    ]
