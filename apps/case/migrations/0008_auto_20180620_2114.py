# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-20 21:14
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case', '0007_auto_20180620_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='create_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='casescript',
            old_name='script_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='case',
            name='is_del',
        ),
        migrations.RemoveField(
            model_name='casescript',
            name='is_del',
        ),
        migrations.AddField(
            model_name='casescript',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='caseset',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='modulecategory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='scriptexcconfig',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='配置名称'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scriptexcconfig',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='case',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 20, 21, 13, 20, 944213), verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='casescript',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 20, 21, 13, 20, 945409), verbose_name='修改时间'),
        ),
    ]
