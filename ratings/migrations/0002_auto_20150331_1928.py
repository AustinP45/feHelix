# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comment', models.TextField()),
                ('review_date', models.DateField()),
                ('overall_rating', models.PositiveSmallIntegerField()),
                ('qual_of_doc', models.PositiveSmallIntegerField()),
                ('efficacy', models.PositiveSmallIntegerField()),
                ('usability', models.PositiveSmallIntegerField()),
                ('tool_id', models.ForeignKey(to='ratings.Tool')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='tool_id',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
