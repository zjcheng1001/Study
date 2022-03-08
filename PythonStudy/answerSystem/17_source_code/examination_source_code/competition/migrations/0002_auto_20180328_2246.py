# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-28 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankinfo',
            name='bank_name',
            field=models.CharField(blank=True, help_text='题库名称', max_length=40, null=True, verbose_name='题库名称'),
        ),
        migrations.AddField(
            model_name='bankinfo',
            name='uid',
            field=models.CharField(blank=True, db_index=True, help_text='用户唯一标识', max_length=32, null=True, verbose_name='用户id'),
        ),
        migrations.AlterField(
            model_name='bankinfo',
            name='bank_type',
            field=models.IntegerField(choices=[(0, '技术类'), (1, '教育类'), (2, '文化类'), (3, '常识类'), (6, '地理类'), (7, '体育类'), (4, '面试题')], default=0, help_text='题库类型', verbose_name='题库类型'),
        ),
    ]