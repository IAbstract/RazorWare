"""
"""
__author__ = 'David Boarman, RazorWare, LLC'

from django.apps import AppConfig


def get_databases():
    from django.db.models import Q
    from RazorCRM_App.models import Company

    companies = Company.objects.filter(~Q(db_name="razorcrm"))

    for company in companies:
        yield {company.db_name: {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': company.db_name,
            'USER': 'root',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
            'PORT': '3306',
            }
        }


class RzAppConfig(AppConfig):
    name = "RazorCRM_App"

    def ready(self):
        from RazorWare_Web.settings import DATABASES
        for db_entry in get_databases():
            DATABASES.update(db_entry)