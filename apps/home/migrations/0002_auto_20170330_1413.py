# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersaccount',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usersaccount',
            name='firstLocation',
        ),
        migrations.RemoveField(
            model_name='usersaccount',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='usersaccount',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usersaccount',
            name='username',
        ),
    ]