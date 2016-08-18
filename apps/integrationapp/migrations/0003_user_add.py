# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courseapp', '0001_initial'),
        ('loginregapp', '0005_auto_20160815_1342'),
        ('integrationapp', '0002_auto_20160816_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginregapp.Userlog')),
            ],
        ),
    ]
