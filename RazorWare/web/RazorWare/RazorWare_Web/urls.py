from django.contrib import admin
from django.conf.urls import patterns, include, url

from generic.views import home as generic

from RazorWare_Web.views import home
from RazorWare_Web.views import websphere

urlpatterns = patterns('',
                       url(r'^razorcrm', include("RazorCRM_App.urls")),
                       url(r'^samplewebpage', include("SampleWebPage.urls")),
                       url(r'^perfectchoicefoods', include("PerfectChoice.urls")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'websphere/test-drive', websphere.test_drive, name="websphere_test_drive"),
                       url(r'test-drive', websphere.test_drive, name="websphere_test_drive"),
                       url(r'', generic.index, name="index"),
                       url('', home.index, name="rzware_index"),
                       )