"""
"""
__author__ = 'David Boarman on 7/1/2015, (c) 2015, RazorWare, LLC'

import json

from django.shortcuts import render

from RazorCRM_App import CUSTOMER_CONFIGS


def get_websphere_info_page(request):
    page = "razorware/info_websphere.html"
    context = CUSTOMER_CONFIGS['websphere']['context']

    return render(request, page, context)

def test_websphere_forms_designer(request):
    page = "razorware/formdesigner.html"
    context = {
        'mode': "test",
        'designer_title': "TestDrive: WebSphere FormsDesigner",
        'tool_content': json.dumps({
            'label': {
                'html': "<label>Label</label>",
                'tooltip': "Add label element to form.",
            },
        })
    }

    return render(request, page, context)