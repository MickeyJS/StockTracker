# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=4)),
                ('full_name', models.CharField(max_length=20)),
            ],
        ),
    ]