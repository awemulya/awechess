# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-01 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20160531_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
