# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
            ],
            managers=[
                ('Users_manage', django.db.models.manager.Manager()),
            ],
        ),
    ]
