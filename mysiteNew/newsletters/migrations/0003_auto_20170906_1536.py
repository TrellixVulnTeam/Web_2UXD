# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_auto_20170906_1244'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewslettersUser',
            new_name='NewsletterUsers',
        ),
    ]
