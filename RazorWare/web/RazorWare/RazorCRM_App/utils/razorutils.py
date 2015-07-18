__author__ = 'David'

import datetime

from django_countries import Countries

from RazorCRM_App.models import Locale
from RazorCRM_App.models import Address
from RazorCRM_App.models import Company

from RazorCRM_App.constants.crm_constants import AcctInfoKeys
from RazorCRM_App.constants.crm_constants import AddrInfoKeys


def init_zip_table():
    """currently only imports US zip codes from CSV file
    :return:
    """
    import django
    django.setup()

    import csv
    import os

    from RazorCRM_App.models import Locale

    file_path = os.path.join(os.path.dirname(__file__), 'us_zip_codes.txt')

    with open(file_path, newline='') as csv_file:
        zip_reader = csv.reader(csv_file, delimiter=',')
        i = 0
        ##  zip,city,state,latitude,longitude,timezone,dst
        for row in zip_reader:
            zip_code = __stringify_zip(row[0])
            print("[SYS] adding zip code: {0}".format(zip_code))

            city = row[1]
            state = row[2]
            lat = row[3]
            lon = row[4]
            tz_offset = row[5]

            Locale.create(zip_code, city, state, lat, lon, tz_offset, "US")

            i += 1

    print("[SYS] import zip codes complete: {0}".format(i))


def get_countries_list():
    countries = Countries()
    country_list = {}

    for code, name in list(countries):
        code_name = "[{0}] {1}".format(code, name)
        print("[APP] adding: {0}".format(code_name))

        country_list[code] = code_name

    return country_list


def gen_comp_acct_num(company_name, address):
    import uuid
    suffix = str(uuid.uuid1()).split("-")[0]

    addr_set = str(address).split(" ")
    # for now assume first element is numeric
    prefix = addr_set[0]

    comp_abbr = str(company_name).lower()[0:3]

    return "{0}-{1}-{2}".format(prefix, comp_abbr, suffix)


def create_company_account(acct_info):
    address = acct_info[AcctInfoKeys.ADDRESS]
    acct_num = gen_comp_acct_num(acct_info[AcctInfoKeys.NAME],
                                 address[AddrInfoKeys.ADDR_LINE_1])
    date_created = datetime.datetime.utcnow()
    company = Company(name=acct_info["name"],
                      account=acct_num,
                      db_name=acct_num,
                      db_created=date_created,
                      is_trial=True)
    company.save()
    company.addresses.add(create_address(address))
    company.save()

    return company


def create_address(addr_info):
    locale = get_or_create_locale(addr_info)
    address = Address(street_addr_1=addr_info[AddrInfoKeys.ADDR_LINE_1],
                      street_addr_2=addr_info[AddrInfoKeys.ADDR_LINE_2],
                      locale=locale)
    address.save()

    return address


def get_or_create_locale(addr_info):
    locale_set = Locale.objects.filter(post_code=addr_info[AddrInfoKeys.POSTAL])

    if not locale_set:
        locale = Locale(addr_info[AddrInfoKeys.CITY],
                        addr_info[AddrInfoKeys.STATE],
                        addr_info[AddrInfoKeys.POSTAL],
                        addr_info[AddrInfoKeys.COUNTRY])
        locale.save()

    else:
        locale = locale_set[0]

    return locale


def try_get_company(company_acct_num):
    companies = Company.objects.filter(account=company_acct_num)
    if companies:
        return [companies]
    else:
        return False


def __stringify_zip(zip_string):
    """Pads zip codes with leading "0" to max length of 5
    :param zip_string: value read from CSV
    :return: normalized zip string with max length of 5
    """
    zip_string = zip_string.zfill(5)

    return zip_string

