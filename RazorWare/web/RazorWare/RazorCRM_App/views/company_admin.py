"""
"""
__author__ = 'David Boarman, RazorWare, LLC'


import json

from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict

from RazorCRM_App.models import Locale

from RazorCRM_App.constants.crm_constants import AddressType

from RazorCRM_App.utils.razorutils import get_countries_list
from RazorCRM_App.utils.razorutils import create_company_account


def get_account_manager(request, acct_id):
    context = {
        'data': {
            'acct_id': acct_id
        }
    }

    return render(request, "razor_app/accountadmin.html", context)