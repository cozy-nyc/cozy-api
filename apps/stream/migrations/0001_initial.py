# Generated by Django 2.0.1 on 2018-08-18 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Stream', max_length=100)),
                ('description', models.TextField()),
                ('channel', models.CharField(blank=True, max_length=100)),
                ('service', models.CharField(blank=True, max_length=100)),
                ('live', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('viewers', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
