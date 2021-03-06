# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-21 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='env_type',
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(choices=[('android_mobile', '安卓手机'), ('android_pos', '安卓POS'), ('android_pad', '安卓PAD'), ('ios', 'ios设备'), ('pc', '电脑'), ('network', '网络设备'), ('other', '其他')], default='android', max_length=20, verbose_name='设备类型'),
        ),
    ]
