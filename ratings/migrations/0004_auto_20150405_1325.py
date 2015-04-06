# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20150405_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='review_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
