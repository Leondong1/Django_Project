# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-11 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='logo',
            field=models.ImageField(null=True, upload_to='booktest', verbose_name='图片'),
        ),
    ]
