"""
"""
__author__ = 'David Boarman, RazorWare, LLC'

from django.conf.urls import url, patterns

from generic.views import home as generic

from PerfectChoice.views import home

from RazorCRM_App.views import login

urlpatterns = patterns('',
                       url(r'', generic.index, name="index"),
                       url(r'rz_login', login.get_web_login, name="rz_login")
                       )
