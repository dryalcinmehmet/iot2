# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stark', '0004_auto_20180107_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseform',
            name='db_ip',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='databaseform',
            name='db_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='databaseform',
            name='db_port',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='databaseform',
            name='kullanici_adi',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='databaseform',
            name='parola',
            field=models.CharField(max_length=10),
        ),
    ]
