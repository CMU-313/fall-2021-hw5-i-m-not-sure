# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-22 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_metadata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemetadataentry',
            name='key',
            field=models.CharField(db_index=True, help_text='Name of the file metadata entry.', max_length=255, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='filemetadataentry',
            name='value',
            field=models.CharField(db_index=True, help_text='Value of the file metadata entry.', max_length=255, verbose_name='Value'),
        ),
    ]
