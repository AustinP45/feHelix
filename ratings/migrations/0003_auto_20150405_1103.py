# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20150331_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='comment',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
