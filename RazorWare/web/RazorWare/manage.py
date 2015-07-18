#!/usr/bin/env python
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if __name__ == "__main__":
    print("[SYS] base dir: {0}".format(BASE_DIR))
    sys.path.append(os.path.join(BASE_DIR, 'RazorWare\\RazorWare_Web\\'))
    print("[SYS] system path: {0}".format(sys.path))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RazorWare_Web.settings")

    from django.core.management import execute_from_command_line

    if '--import_zips' in sys.argv:
        sys.argv.remove('--import_zips')
        from RazorCRM_App.utils.razorutils import init_zip_table as init_zips
        init_zips()

        if 'runserver' not in sys.argv:
            sys.exit(0)

    execute_from_command_line(sys.argv)
