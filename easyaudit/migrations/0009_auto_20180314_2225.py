# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-14 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyaudit', '0008_auto_20180220_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestevent',
            name='query_string',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='requestevent',
            name='url',
            field=models.TextField(),
        ),
    ]
