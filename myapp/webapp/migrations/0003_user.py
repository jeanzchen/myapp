# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20160531_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=128)),
                ('lname', models.CharField(max_length=128)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.UserCategory')),
            ],
        ),
    ]
