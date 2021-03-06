# Generated by Django 3.2.7 on 2021-10-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_users_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
