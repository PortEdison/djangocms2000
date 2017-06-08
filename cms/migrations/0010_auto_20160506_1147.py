# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20160308_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('ja', 'Japanese'), ('fr', 'French'), ('es', 'Spanish'), ('pt', 'Portuguese')], default='en', max_length=5),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(blank=True, upload_to='cms_dev/%y_%m'),
        ),
    ]
