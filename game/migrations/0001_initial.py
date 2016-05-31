# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-30 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=256)),
                ('site', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('round', models.FloatField()),
                ('result', models.CharField(max_length=10)),
                ('white_elo', models.IntegerField()),
                ('black_elo', models.IntegerField()),
                ('eco', models.CharField(max_length=10)),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move_no', models.IntegerField()),
                ('white', models.CharField(max_length=10)),
                ('black', models.CharField(max_length=10)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moves', to='game.GameData')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='gamedata',
            name='black',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='black', to='game.Player'),
        ),
        migrations.AddField(
            model_name='gamedata',
            name='white',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='white', to='game.Player'),
        ),
    ]