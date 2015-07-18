"""
"""
__author__ = 'David Boarman, RazorWare, LLC'


from django.shortcuts import render

from RazorCRM_App.views.queries import COUNTRIES
from RazorCRM_App.views.queries import ADDRESS_TYPES_INFO


def index(request):
    context = {
        'data': {
            'countries': COUNTRIES,
            'addr_types': ADDRESS_TYPES_INFO
        }
    }

    return render(request, "razorware/home.html", context)


