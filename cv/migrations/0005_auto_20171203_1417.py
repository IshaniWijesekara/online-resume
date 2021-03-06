# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_personalinfo_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='interest',
            field=models.CharField(blank=True, help_text='Sparate interests by comma', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='language',
            field=models.CharField(blank=True, help_text='Sparate languages by comma', max_length=200, null=True),
        ),
    ]
