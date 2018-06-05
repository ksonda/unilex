# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0003_vocabulary_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='private',
            field=models.BooleanField(
                default=True,
                help_text='Private vocabulary can be edited only by the users belonging to its authority.',
                verbose_name='Private vocabulary'
            ),
        ),
    ]
