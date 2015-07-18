__author__ = 'David'


class AcctInfoKeys:
    NAME = "name"
    ADDRESS = "address"


class AddrInfoKeys:
    ADDR_LINE_1 = "line_1"
    ADDR_LINE_2 = "line_2"
    CITY = "city"
    STATE = "state"
    POSTAL = "postal"
    COUNTRY = "country"


class AddressType:
    HOME = 1
    BUSINESS = 2
    MAILING = 4
    BILLING = 8
    SECONDARY = 16
    SHIPPING = 32
    PHYSICAL = 64

    DEFAULT_CHOICES = {
        'Home.Primary': HOME | BILLING | MAILING,
        'Home Mailing': HOME | MAILING,
        'Home.Billing': HOME | BILLING,
        'Home.Secondary': HOME | SECONDARY,
        'Business.Primary': BUSINESS | BILLING | MAILING,
        'Business.Mailing': BUSINESS | MAILING,
        'Business.Billing': BUSINESS | BILLING,
        'Shipping': SHIPPING
    }

    DEFAULT_DESCRIPTIONS = {
        'Home.Primary': "Primary Home Billing & Mailing Address",
        'Home Mailing': "Home Mailing Address",
        'Home.Billing': "Home Billing Address",
        'Home.Secondary': "Secondary Home Address",
        'Business.Primary': "Primary Business Billing & Mailing Address",
        'Business.Mailing': "Business Mailing Address",
        'Business.Billing': "Business Billing Address",
        'Shipping': "Shipping (Ship-To) Address",
        'Other': "Other Address"
    }

    @classmethod
    def get_addr_display(cls, value):
        addr_key = None

        for key, val in AddressType.DEFAULT_CHOICES.items():
            if val == value:
                addr_key = key
                break

        return addr_key

    @classmethod
    def get_addr_description(cls, value):
        addr_key = AddressType.get_addr_display(value)
        addr_descr = ""

        if addr_key:
            addr_descr = AddressType.DEFAULT_DESCRIPTIONS[addr_key]

        return addr_descr

