# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_event_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reader',
            field=models.FileField(default='', upload_to=''),
        ),
    ]