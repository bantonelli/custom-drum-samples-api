# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitbuilder', '0007_kitdescription_number_of_samples'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitdescription',
            name='selling_point1_title',
            field=models.CharField(default='Selling Point Title', max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kitdescription',
            name='selling_point2_title',
            field=models.CharField(default='Selling Point 2 Title', max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kitdescription',
            name='selling_point3_title',
            field=models.CharField(default='Selling Point 3 Title', max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
