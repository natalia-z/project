# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puddlesbooking', '0003_auto_20170423_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
