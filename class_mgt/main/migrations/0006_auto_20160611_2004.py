# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_notification_n_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='p_is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
