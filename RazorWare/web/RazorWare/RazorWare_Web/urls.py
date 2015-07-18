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
                       url(r'websphere/getWebSphereInfo', websphere.get_websphere_info_page, name="get_websphere_info_page"),
                       url(r'getWebSphereInfo', websphere.get_websphere_info_page, name="get_websphere_info_page"),
                       url(r'getTestFormsDesigner', websphere.test_websphere_forms_designer, name="get_websphere_forms_designer"),
                       url(r'', generic.index, name="index"),
                       url('', home.index, name="rzware_index"),
                       )