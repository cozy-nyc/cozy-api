# Generated by Django 2.2.2 on 2019-08-03 20:54

import apps.exchange.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('material', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('lastActive', models.DateTimeField(default=django.utils.timezone.now)),
                ('visible', models.BooleanField(default=True)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('primaryImage', models.ImageField(upload_to='images/')),
                ('imageCount', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item', to='exchange.Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ('-lastActive',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountExchanged', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deliveryAddress', models.TextField()),
                ('receiveAddress', models.TextField()),
                ('timeSold', models.DateTimeField(auto_now=True)),
                ('ratingSeller', models.DecimalField(decimal_places=1, max_digits=1)),
                ('ratingBuyer', models.DecimalField(decimal_places=1, max_digits=1)),
                ('isValid', models.BooleanField(default=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Buyer', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item', to='exchange.Item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to=apps.exchange.models.scramble_uploaded_filename)),
                ('index', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='exchange.Item')),
            ],
        ),
    ]
