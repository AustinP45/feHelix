# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_auto_20150405_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='review_count',
        ),
    ]
