# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitbuilder', '0006_customkit_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitdescription',
            name='number_of_samples',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
