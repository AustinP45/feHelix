# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('desc', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('comment', models.TextField()),
                ('overall_rating', models.PositiveSmallIntegerField()),
                ('qual_of_doc', models.PositiveSmallIntegerField()),
                ('efficacy', models.PositiveSmallIntegerField()),
                ('usability', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('link', models.URLField(max_length=100)),
                ('overall_score', models.DecimalField(decimal_places=3, max_digits=4)),
                ('qual_of_doc', models.DecimalField(decimal_places=3, max_digits=4)),
                ('efficacy', models.DecimalField(decimal_places=3, max_digits=4)),
                ('usability', models.DecimalField(decimal_places=3, max_digits=4)),
                ('free', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
                ('review_count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ToolCat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('cat_id', models.ForeignKey(to='ratings.Category')),
                ('tool_id', models.ForeignKey(to='ratings.Tool')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rating',
            name='tool_id',
            field=models.ForeignKey(to='ratings.Tool'),
            preserve_default=True,
        ),
    ]
