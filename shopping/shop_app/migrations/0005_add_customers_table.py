# Generated by Django 2.0.2 on 2018-03-22 02:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_add_inventory_on_hand_field-products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Enter a valid 10 digit phone number starting with the area code', regex='^\\d{10}$')])),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_addresses', to='shop_app.Address')),
                ('shipping_address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_addresses', to='shop_app.Address')),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]
