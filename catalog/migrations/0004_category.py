# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('catalog', models.ManyToManyField(to='catalog.Catalog')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
