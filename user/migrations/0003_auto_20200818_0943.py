# Generated by Django 3.1 on 2020-08-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(max_length=50),
        ),
    ]