# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitbuilder', '0005_auto_20141226_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='customkit',
            name='tags',
            field=models.ManyToManyField(to='kitbuilder.Tag'),
            preserve_default=True,
        ),
    ]
