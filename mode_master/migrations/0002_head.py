# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-30 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mode_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
    ]
