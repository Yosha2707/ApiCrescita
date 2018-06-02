# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-30 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modify_by', models.IntegerField(default=0)),
                ('modify_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]