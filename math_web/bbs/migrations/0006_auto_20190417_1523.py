# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0005_auto_20190414_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
