__author__ = 'David Boarman on 6/23/2015, (c) 2015, RazorWare, LLC'

import json

from RazorCRM_App.models import UserAccount

from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_user(request):
    data = json.loads(request.body.decode('utf-8'))
    print("received request: {data}".format(data=data))

    try:
        user_id = data['user_id']
        password = data['password']
    except Exception as ex:
        print("exception: {ex}".format(ex=ex.__str__()))

    if user_id:
        print("request: log in user [{user}]".format(user=user_id))
        accounts = UserAccount.objects.filter(Q(user_id=user_id)|Q(password=password))
        if accounts and len(accounts) == 1:
            user_account = accounts[0]

        data = {
            'result': user_account is not None,
            'active': "invalid" if user_account is None else user_account.enabled,
            'reset': "invalid" if user_account is None else user_account.reset,
            'acct_id': "invalid" if user_account is None else user_account.company.account
        }
    else:
        data = {
            'result': False,
            'err': "invalid credential"
        }

    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response