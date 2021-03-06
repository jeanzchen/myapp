# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 02:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('LogId', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=128)),
                ('lname', models.CharField(max_length=128)),
                ('UserToVisit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.User')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.UserCategory')),
            ],
        ),
    ]
