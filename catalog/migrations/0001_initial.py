# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
                ('manufacturer', models.CharField(blank=True, max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
