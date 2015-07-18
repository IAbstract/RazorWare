__author__ = 'David Boarman on 6/25/2015, (c) 2015, RazorWare, LLC'

import json

from django.shortcuts import render

from RazorCRM_App.models import UserAccount

from RazorCRM_App.views.mobile.rzm_login import login_user


def get_web_login(request):
    return render(request, "razor_app/userlogin.html")


def web_login(request):
    pass