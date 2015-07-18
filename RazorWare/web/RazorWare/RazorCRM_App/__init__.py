"""
"""
__author__ = 'David Boarman, RazorWare, LLC'

import json


default_app_config = 'RazorCRM_App.rz_app_config.RzAppConfig'

CUSTOMER_CONFIGS = {
    'websphere': {
        'context': {
            'cust_title': "RazorWare WebSphere",
            'cust_stylesheet': "style.css",
            'cust_header': "images/rz_websphere_header.png",
            'cust_message': "RazorWare WebSphere: Redefining Your WebSphere of Influence.",
            'menu': json.dumps({
                'opts_order': ['home:75', 'contact:75', 'space:25', 'websphere:125', 'space:25', 'login:25'],
                'login': "images/btn_login.png",
                'home': "images/btn_home.png",
                'contact': "images/btn_contact.png",
                'websphere': "images/btn_websphere.png",
                'tips': {
                    'login': "Click to login to RzWare CRM.",
                    'websphere': "Click to learn more about WebSphere."
                }
            }),
        },
        'home': "razorware/home.html"
    },
    'perfectchoicefoods': {
        'context': {
            'cust_title': "PerfectChoice Foods",
            'cust_stylesheet': "PerfectChoice/style.css",
            'cust_header': "images/PerfectChoice/perfchoice_header.png",
            'cust_message': "Welcome to PerfectChoice Foods",
            'menu': json.dumps({
                'opts_order': ['home:75', 'contact:75', 'space:25', 'recipes:75', 'login:25'],
                'login': "images/btn_login.png",
                'home': "images/PerfectChoice/btn_home.png",
                'contact': "images/PerfectChoice/btn_contact.png",
                'recipes': "images/PerfectChoice/btn_recipes.png",
                'sub_opts': {
                    'recipes': ['Poultry', 'Beef', 'separator', 'Submit']
                }
            }),
        },
        'home': "PerfectChoice/home.html"
    },
    'samplewebpage': {
        'context': {
            'cust_title': "Sample Customer Page",
            'cust_stylesheet': "SampleWeb/style.css",
            'cust_header': "images/SampleWeb/sample_header.png",
            'cust_message': "Welcome to Sample Web Page",
            'menu': json.dumps({
                'opts_order': ['home:75', 'styles:75', 'contact:75', 'login:25'],
                'login': "images/btn_login.png",
                'home': "images/SampleWeb/btn_home.png",
                'styles': "images/SampleWeb/btn_style.png",
                'contact': "images/SampleWeb/btn_contact.png",
                'sub_opts': {
                    'styles': ['Default', 'Custom']
                }
            }),
        },
        'home': "SampleWebPage/home.html"
    },
}
