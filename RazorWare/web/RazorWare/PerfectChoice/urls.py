"""
"""
__author__ = 'David Boarman, RazorWare, LLC'

from django.conf.urls import url, patterns

from generic.views import home as generic

from PerfectChoice.views import home

from RazorCRM_App.views import login

urlpatterns = patterns('',
                       url(r'', generic.index, name="index"),
                       )
