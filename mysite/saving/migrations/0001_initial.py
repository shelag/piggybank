# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date_pub', models.DateField(verbose_name='Data inserimento', auto_now_add=True)),
                ('text', models.CharField(verbose_name='Descrizione', max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD')], max_length=3)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('word', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='movement',
            name='tag',
            field=models.ManyToManyField(to='saving.Tag'),
        ),
    ]
