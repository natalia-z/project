# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puddlesbooking', '0016_theme_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='addon',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]