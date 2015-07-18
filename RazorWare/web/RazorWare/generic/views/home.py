__author__ = 'David Boarman on 6/25/2015, (c) 2015, RazorWare, LLC'

from django.shortcuts import render
from django.views.generic import RedirectView

from RazorCRM_App import CUSTOMER_CONFIGS


def index(request):
    path = request.path.replace("/", "")
    if path == "":
        path = "websphere"

    print("[RzWeb] path => {path}".format(path=path))

    context = CUSTOMER_CONFIGS[path]['context']
    page = CUSTOMER_CONFIGS[path]['home']

    return render(request, page, context)
