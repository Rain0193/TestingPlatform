# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-03 20:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0020_auto_20180703_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 3, 20, 26, 4, 77331), verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='casescript',
            name='execute_env',
            field=models.CharField(help_text='产品型号如:android_mobile,android_pos,computer...', max_length=200, verbose_name='执行环境'),
        ),
        migrations.AlterField(
            model_name='casescript',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 3, 20, 26, 4, 78756), verbose_name='修改时间'),
        ),
    ]
