# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 15:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EnterprisesApp', '0003_auto_20170731_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprises',
            name='description',
        ),
    ]