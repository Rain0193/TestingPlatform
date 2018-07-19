# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-16 17:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataconfig', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlDataConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('url', models.CharField(max_length=300, verbose_name='域名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'url数据配置',
                'verbose_name_plural': 'url数据配置',
            },
        ),
        migrations.RemoveField(
            model_name='testdataconfig',
            name='web_url',
        ),
        migrations.AddField(
            model_name='urldataconfig',
            name='test_data_config',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='dataconfig.TestDataConfig', verbose_name='测试数据配置'),
        ),
    ]
