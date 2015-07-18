"""
"""
__author__ = 'David Boarman, RazorWare, LLC'


import json

from django.http import HttpResponse
from django.forms.models import model_to_dict

from RazorCRM_App.models import Locale

from RazorCRM_App.constants.crm_constants import AddressType

from RazorCRM_App.utils.razorutils import get_countries_list
from RazorCRM_App.utils.razorutils import create_company_account

COUNTRIES = get_countries_list()
ADDRESS_TYPES_INFO = AddressType.DEFAULT_DESCRIPTIONS


def query_locales(request):
    post_code = request.GET.get("post_code")
    print("[QUERIES] query local by zip/post code: {0}".format(post_code))

    data = {}
    locale = Locale.objects.filter(post_code=post_code)
    if locale:
        data['success'] = True
        data['location'] = model_to_dict(locale[0], [], [])
        #   location.country is not json serializable - assign country code
        data['location']['country'] = data['location']['country'].code
    else:
        #   TODO:   add post code and locale info
        data['success'] = False
        data['location'] = {}

    return HttpResponse(json.dumps(data), content_type="application/json")


def create_account(request):
    acct_info = json.loads(request.GET.get("trial_info"))
    comp_info = acct_info["company"]
    cont_info = acct_info["contact"]

    data = {
        'success': False
    }

    print("[QUERIES] creating account: {0}".format(comp_info["name"]))
    try:
        company = create_company_account(comp_info)

        data['company'] = {
            'account': company.account
        }
        data['success'] = True

    except Exception as ex:
        data['err_msg'] = ex.__str__()
        data['success'] = False

    print("[QUERIES] adding primary contact: {0}, {1}".format(cont_info["sname"], cont_info["fname"]))

    return HttpResponse(json.dumps(data), content_type="application/json")


def get_account_info(request):
    acct_id = request.GET.get("acct_id")

    data = {
        'acct_id': acct_id
    }

    return HttpResponse(json.dumps(data), content_type="application/json")