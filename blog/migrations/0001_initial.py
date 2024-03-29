# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-17 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('content', tinymce.models.HTMLField()),
            ],
            managers=[
                ('text_manage', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('pwd', models.CharField(default='12345678', max_length=32)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('sex', models.CharField(default='男', max_length=3)),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('head', models.ImageField(default='/static/blog/img/icon.png', upload_to='static/blog/userimg/')),
            ],
            managers=[
                ('Users_manage', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='text',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.users'),
        ),
    ]
