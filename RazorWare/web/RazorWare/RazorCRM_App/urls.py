"""
"""
__author__ = 'David Boarman, RazorWare, LLC'

from django.conf.urls import url, patterns

from RazorWare_Web.views import home

from RazorCRM_App.views import login
from RazorCRM_App.views import queries
from RazorCRM_App.views import company_admin
from RazorCRM_App.views.mobile import rzm_login

urlpatterns = patterns('',
                       url(r'', home.index, name="index"),
                       url(r'^rz_login/$', login.get_web_login, name="web_login_user"),
                       url(r'rzm_login', rzm_login.login_user, name="mobile_login_user"),
                       url(r'^query_locale/$', queries.query_locales, name="query_locales"),
                       url(r'^start_trial/$', queries.create_account, name="create_account"),
                       url(r'^query_account/$', queries.get_account_info, name="get_account_info"),
                       url(r'(?P<acct_id>.*)/admin', company_admin.get_account_manager, name="get_account_manager"),
                       )
