# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-30 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('raw_packing_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_code', models.CharField(max_length=100)),
                ('factory_name', models.CharField(max_length=100)),
                ('pack_size', models.CharField(max_length=100)),
                ('rt_id', models.IntegerField(default=0)),
                ('rawmultiplier', models.FloatField(default=0)),
                ('wastage', models.FloatField(default=0)),
                ('overall_wastage', models.FloatField(default=0)),
                ('margin_per', models.FloatField(default=0)),
                ('margin_amount', models.FloatField(default=0)),
                ('mrp_per', models.FloatField(default=0)),
                ('mrp_price', models.FloatField(default=0)),
                ('Raw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raw_packing_master.raw')),
            ],
        ),
    ]
