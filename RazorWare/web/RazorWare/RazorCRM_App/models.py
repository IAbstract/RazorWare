__copyright = "c 2014, RazorWare, LLC"
__author__ = "David Boarman"

import datetime

from django.db import models
from django_countries.fields import CountryField

from RazorCRM_App.constants.crm_constants import AddressType


class Locale(models.Model):
    id = models.AutoField(primary_key=True)

    post_code = models.CharField(db_column="post_code", max_length=10, unique=True, blank=False)
    city = models.CharField(db_column="city", max_length=128, blank=False)
    state_region = models.CharField(db_column="state_region", max_length=5, blank=False)
    latitude = models.FloatField(db_column="latitude", blank=False, default=0.0)
    longitude = models.FloatField(db_column="longitude", blank=False, default=0.0)
    tz_offset = models.SmallIntegerField(db_column="tz_offset", blank=False, default=0)
    country = CountryField()

    @classmethod
    def create(cls, code, city, st_reg, lat, lon, tz_offset, country):

        ##  create and save locale
        locale = cls(post_code=code,
                     city=city,
                     state_region=st_reg,
                     latitude=lat,
                     longitude=lon,
                     tz_offset=tz_offset,
                     country=country)
        locale.save()

        return locale


class Person(models.Model):
    id = models.AutoField(primary_key=True)

    forename = models.CharField(db_column="forename", max_length=64, blank=False)
    middle_name = models.CharField(db_column="middle_name", max_length=64, blank=True)
    surname = models.CharField(db_column="surname", max_length=64, blank=False)
    addresses = models.ManyToManyField("Address")
    phones = models.ManyToManyField("ContactPhone")
    emails = models.ManyToManyField("ContactEmail")
    groups = models.ManyToManyField("Group")

    def __str__(self):
        return "{0}, {1}".format(self.surname, self.forename)


class Address(models.Model):
    id = models.AutoField(primary_key=True)

    street_addr_1 = models.CharField(db_column="street_address1", max_length=256, blank=False)
    street_addr_2 = models.CharField(db_column="street_address2", max_length=256, blank=True)
    locale = models.ForeignKey("Locale")
    address_type = models.IntegerField(db_column="address_type", default=AddressType.DEFAULT_CHOICES['Home.Primary'])
    primary_physical = models.BooleanField(db_column="primary_physical", blank=False, default=False)

    def __str__(self):
        return self.street_addr_1


class ContactEmail(models.Model):
    PRIMARY = 0
    ADDITIONAL = 1

    id = models.AutoField(primary_key=True)

    email = models.CharField(db_column="primary_phone", max_length=12, blank=False)
    email_type = models.IntegerField(db_column="type", )


class ContactPhone(models.Model):
    PRIMARY = 0
    ADDITIONAL = 1
    CELL = 2

    id = models.AutoField(primary_key=True)

    phone = models.CharField(db_column="primary_phone", max_length=12, blank=False)
    phone_type = models.IntegerField(db_column="type", )

    def __str__(self):
        return str(self.primary_phone)


class Company(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(db_column="name", max_length=128, blank=False)
    account = models.CharField(db_column="acct_num", max_length=32, blank=False, unique=True, default="00000-xxx-00000-0")
    addresses = models.ManyToManyField(Address)
    contacts = models.ManyToManyField(Person)
    groups = models.ManyToManyField("Group")
    db_name = models.CharField(db_column="db_name", max_length=64, unique=True, blank=False, default="new_database")
    db_created = models.DateField(db_column="db_created", blank=False, default=datetime.datetime.utcnow())
    is_trial = models.BooleanField(db_column="is_trial", blank=False, default=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(db_column="name", max_length=64, blank=False)
    email = models.CharField(db_column="email", max_length=128, blank=True)
    site = models.CharField(db_column="site", max_length=128, blank=False)
    lead = models.OneToOneField(Person)
    team = models.ManyToManyRel(Person)
    owner = models.OneToOneField(Company)

    def __str__(self):
        return self.name

class UserAccount(models.Model):
    id = models.AutoField(primary_key=True)

    person = models.ForeignKey("Person")
    user_id = models.CharField(db_column="user_id", max_length=16, blank=False, null=False)
    password = models.CharField(db_column="password", max_length=32, blank=False, null=False)
    enabled = models.BooleanField(db_column="enabled", blank=False, default=True)
    reset = models.BooleanField(db_column="reset", blank=False, default=False)
    set_date = models.DateField(db_column="set_date")
    company = models.ForeignKey("Company")