# Generated by Django 3.2.7 on 2021-10-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_users_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, verbose_name='Активный'),
        ),
    ]