# Generated by Django 4.2.1 on 2023-05-25 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechile_app', '0002_remove_user_is_admin_remove_user_is_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]+$', 'Only alphanumeric characters are allowed.')])),
                ('vehicle_type', models.CharField(choices=[('1', 'Two Wheelers'), ('2', 'Three Wheelers'), ('3', 'Four Wheelers')], max_length=1)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_description', models.TextField()),
            ],
        ),
    ]