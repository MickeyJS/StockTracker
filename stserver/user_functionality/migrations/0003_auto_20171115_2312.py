# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_functionality', '0002_remove_user_tel_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlesubscription',
            name='change_value',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='singlesubscription',
            name='date_from',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='singlesubscription',
            name='date_to',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='tel_number',
            field=models.IntegerField(default=123456789),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
