# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='locations',
            field=models.CharField(default='My Location default', max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
    ]
