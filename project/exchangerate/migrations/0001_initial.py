# Generated by Django 3.2.1 on 2021-11-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency_code', models.CharField(max_length=3)),
                ('from_currency_name', models.CharField(max_length=50)),
                ('to_currency_code', models.CharField(max_length=3)),
                ('to_currency_name', models.CharField(max_length=50)),
                ('exchange_rate', models.DecimalField(decimal_places=8, max_digits=17)),
                ('last_refreshed', models.DateTimeField()),
                ('time_zone', models.CharField(max_length=3)),
                ('bid_price', models.DecimalField(decimal_places=8, max_digits=17)),
                ('ask_price', models.DecimalField(decimal_places=8, max_digits=17)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
