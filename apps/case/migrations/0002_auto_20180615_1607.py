# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-15 16:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='update_time',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 16, 7, 45, 902955), verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='casescript',
            name='update_time',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 16, 7, 45, 903991), verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(default='', help_text='产品code', max_length=30, verbose_name='产品code'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(default='', help_text='产品描述', verbose_name='产品描述'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', help_text='产品名', max_length=30, verbose_name='产品名'),
        ),
    ]