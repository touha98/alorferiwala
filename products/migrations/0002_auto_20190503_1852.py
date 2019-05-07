# Generated by Django 2.2.1 on 2019-05-03 12:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_owner',
            field=models.ForeignKey(blank=True, default=12, on_delete=django.db.models.deletion.CASCADE, related_name='product_seller', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='init_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=12, upload_to='photos/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sold_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('OS', 'On Sale'), ('OD', 'Ordered'), ('SD', 'Sold')], default='OS', max_length=2),
        ),
        migrations.AddField(
            model_name='product',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]