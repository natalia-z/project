# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('confirmed', 'CONFIRMED'), ('cancelled', 'CANCELLED'), ('submitted', 'SUBMITTED'), ('paid', 'PAID')], max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=100)),
                ('children_names', models.CharField(max_length=200)),
                ('male_female', models.CharField(choices=[('g', 'Girls'), ('b', 'Boys'), ('mix', 'Mix')], max_length=10)),
                ('children_ages', models.CharField(max_length=200)),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('post_code', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('number_of_children', models.CharField(choices=[('xs', 'Up to 10'), ('s', '11 - 14'), ('m', '15 - 19'), ('l', '20 - 24'), ('xl', '25 - 30')], max_length=10)),
                ('number_of_babies', models.PositiveIntegerField(blank=True, null=True)),
                ('dietary_requirements', models.CharField(blank=True, choices=[('none', 'None'), ('veggie', 'Veggie'), ('vegan', 'Vegan'), ('halal', 'Halal'), ('kosher', 'Kosher'), ('no_chocolate', 'No chocolate coins')], max_length=50, null=True)),
                ('allergies', models.CharField(blank=True, max_length=300, null=True)),
                ('flexible_dates', models.BooleanField(default=True)),
                ('other', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingAddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_on', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='puddlesbooking.AddOn')),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='puddlesbooking.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day_of_week', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(default='description default text')),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('post_code', models.CharField(max_length=200)),
                ('parking', models.CharField(blank=True, default='parking default text', max_length=120, null=True)),
                ('group_min', models.IntegerField(default=5)),
                ('group_max', models.IntegerField(default=25)),
                ('catering', models.BooleanField(default=True)),
                ('own_food', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='timeslot',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puddlesbooking.Venue'),
        ),
        migrations.AddField(
            model_name='booking',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='puddlesbooking.Theme'),
        ),
        migrations.AddField(
            model_name='booking',
            name='timeslot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='puddlesbooking.Timeslot'),
        ),
    ]
