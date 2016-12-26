# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmClock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='alarmclock',
            name='dayofweek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.DayOfWeek'),
        ),
        migrations.AddField(
            model_name='alarmclock',
            name='webradio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.WebRadio'),
        ),
    ]
