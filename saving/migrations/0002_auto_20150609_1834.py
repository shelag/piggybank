# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='date_pub',
            field=models.DateField(verbose_name='Data inserimento', default=django.utils.timezone.now),
        ),
    ]
