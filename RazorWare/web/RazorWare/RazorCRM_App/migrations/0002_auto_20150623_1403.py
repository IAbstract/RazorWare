# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RazorCRM_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.CharField(db_column='user_id', max_length=16)),
                ('password', models.CharField(db_column='password', max_length=32)),
                ('enabled', models.BooleanField(db_column='enabled', default=True)),
                ('reset', models.BooleanField(db_column='reset', default=False)),
                ('set_date', models.DateField(db_column='set_date')),
                ('person', models.ForeignKey(to='RazorCRM_App.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='company',
            name='db_created',
            field=models.DateField(db_column='db_created', default=datetime.datetime(2015, 6, 23, 21, 3, 45, 893204)),
            preserve_default=True,
        ),
    ]
