# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('street_addr_1', models.CharField(db_column='street_address1', max_length=256)),
                ('street_addr_2', models.CharField(db_column='street_address2', blank=True, max_length=256)),
                ('address_type', models.IntegerField(default=13, db_column='address_type')),
                ('primary_physical', models.BooleanField(default=False, db_column='primary_physical')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=128)),
                ('account', models.CharField(unique=True, default='00000-xxx-00000-0', db_column='acct_num', max_length=32)),
                ('db_name', models.CharField(unique=True, default='new_database', db_column='db_name', max_length=64)),
                ('db_created', models.DateField(default=datetime.datetime(2015, 3, 2, 13, 51, 16, 46902), db_column='db_created')),
                ('is_trial', models.BooleanField(default=True, db_column='is_trial')),
                ('addresses', models.ManyToManyField(to='RazorCRM_App.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(db_column='primary_phone', max_length=12)),
                ('email_type', models.IntegerField(db_column='type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactPhone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(db_column='primary_phone', max_length=12)),
                ('phone_type', models.IntegerField(db_column='type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=64)),
                ('email', models.CharField(db_column='email', blank=True, max_length=128)),
                ('site', models.CharField(db_column='site', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_code', models.CharField(unique=True, db_column='post_code', max_length=10)),
                ('city', models.CharField(db_column='city', max_length=128)),
                ('state_region', models.CharField(db_column='state_region', max_length=5)),
                ('latitude', models.FloatField(default=0.0, db_column='latitude')),
                ('longitude', models.FloatField(default=0.0, db_column='longitude')),
                ('tz_offset', models.SmallIntegerField(default=0, db_column='tz_offset')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('forename', models.CharField(db_column='forename', max_length=64)),
                ('middle_name', models.CharField(db_column='middle_name', blank=True, max_length=64)),
                ('surname', models.CharField(db_column='surname', max_length=64)),
                ('addresses', models.ManyToManyField(to='RazorCRM_App.Address')),
                ('emails', models.ManyToManyField(to='RazorCRM_App.ContactEmail')),
                ('groups', models.ManyToManyField(to='RazorCRM_App.Group')),
                ('phones', models.ManyToManyField(to='RazorCRM_App.ContactPhone')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='lead',
            field=models.OneToOneField(to='RazorCRM_App.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.OneToOneField(to='RazorCRM_App.Company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='contacts',
            field=models.ManyToManyField(to='RazorCRM_App.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='groups',
            field=models.ManyToManyField(to='RazorCRM_App.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='locale',
            field=models.ForeignKey(to='RazorCRM_App.Locale'),
            preserve_default=True,
        ),
    ]
