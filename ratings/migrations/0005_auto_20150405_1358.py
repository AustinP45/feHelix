# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20150405_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='overall_score',
            new_name='overall_rating',
        ),
    ]
