# Generated by Django 3.1 on 2020-09-07 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quoterequest', '0005_quoterequest_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoterequest',
            name='product',
        ),
    ]