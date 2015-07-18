# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RazorCRM_App', '0002_auto_20150623_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='company',
            field=models.ForeignKey(default=1, to='RazorCRM_App.Company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='db_created',
            field=models.DateField(default=datetime.datetime(2015, 6, 24, 12, 11, 34, 69615), db_column='db_created'),
            preserve_default=True,
        ),
    ]
