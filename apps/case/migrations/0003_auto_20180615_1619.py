# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-15 16:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20180615_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulecategory',
            options={'verbose_name': '模块', 'verbose_name_plural': '模块'},
        ),
        migrations.AlterField(
            model_name='case',
            name='update_time',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 16, 19, 54, 944971), verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='casescript',
            name='update_time',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 16, 19, 54, 946112), verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='modulecategory',
            name='code',
            field=models.CharField(default='', help_text='模块code', max_length=30, verbose_name='模块code'),
        ),
        migrations.AlterField(
            model_name='modulecategory',
            name='desc',
            field=models.TextField(default='', help_text='模块描述', verbose_name='模块描述'),
        ),
        migrations.AlterField(
            model_name='modulecategory',
            name='name',
            field=models.CharField(default='', help_text='模块名', max_length=30, verbose_name='模块名'),
        ),
        migrations.AlterField(
            model_name='modulecategory',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.Product', verbose_name='产品'),
        ),
    ]