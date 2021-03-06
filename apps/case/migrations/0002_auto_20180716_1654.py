# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-16 16:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtask',
            name='execut_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_testTask', to=settings.AUTH_USER_MODEL, verbose_name='执行人'),
        ),
        migrations.AddField(
            model_name='testtask',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='modulecategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父类目', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_module_cat', to='case.ModuleCategory', verbose_name='父类目'),
        ),
        migrations.AddField(
            model_name='modulecategory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='modulecategory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='caseset',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caseset', to='case.ModuleCategory', verbose_name='产品模块'),
        ),
        migrations.AddField(
            model_name='caseset',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='casescript',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_script', to='case.Case', verbose_name='测试用例'),
        ),
        migrations.AddField(
            model_name='casescript',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='casereletetesttask',
            name='case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='case.Case', verbose_name='用例'),
        ),
        migrations.AddField(
            model_name='casereletetesttask',
            name='case_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='case.CaseSet', verbose_name='用例集'),
        ),
        migrations.AddField(
            model_name='casereletetesttask',
            name='test_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='case.TestTask', verbose_name='测试任务'),
        ),
        migrations.AddField(
            model_name='casereletecaseset',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.Case', verbose_name='测试用例'),
        ),
        migrations.AddField(
            model_name='casereletecaseset',
            name='case_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='case.CaseSet', verbose_name='用例集'),
        ),
        migrations.AddField(
            model_name='case',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='case.ModuleCategory', verbose_name='产品模块'),
        ),
        migrations.AddField(
            model_name='case',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
    ]
