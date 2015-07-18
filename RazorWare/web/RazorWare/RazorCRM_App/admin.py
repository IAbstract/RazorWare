from django.contrib import admin

# Register your models here.
from RazorCRM_App.models import Address
from RazorCRM_App.models import Locale
from RazorCRM_App.models import Person
from RazorCRM_App.models import ContactPhone
from RazorCRM_App.models import ContactEmail
from RazorCRM_App.models import Company
from RazorCRM_App.models import Group


admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Locale)
admin.site.register(ContactPhone)
admin.site.register(ContactEmail)
admin.site.register(Group)


class LocaleInline(admin.ModelAdmin):
    model = Locale


class AddressAdminInline(admin.ModelAdmin):
    model = Address

    inlines = [LocaleInline]


class ContactPhoneAdminInline(admin.TabularInline):
    model = ContactPhone


class ContactEmailAdminInline(admin.TabularInline):
    model = ContactEmail


class PersonInlineAdmin(admin.TabularInline):
    model = Person


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        ('ID', {
            'fields': ['id']
        }),
        ('Name', {
            'fields': ['name']
        }),
        ('Addresses', {
            'fields': ['addresses']
        }),
        ('Contacts', {
            'fields': ['contacts']
        }),
        ('Database Created', {
            'fields': ['db_created']
        }),
        ('Database Name', {
            'fields': ['db_name']
        }),
        ('Is Trial', {
            'fields': ['is_trial']
        })
    ]
    inlines = [PersonInlineAdmin, AddressAdminInline]


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        ('ID', {
            'fields': ['id']
        }),
        ('Name', {
            'fields': ['name']
        }),
        ('Name', {
            'fields': ['email']
        }),
        ('Lead', {
            'fields': ['lead'],
        }),
        ('Team', {
            'fields': ['team'],
        }),
        ('Company', {
            'fields': ['owner']
        })
    ]
    inlines = ["PersonAdmin", PersonInlineAdmin]


class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        ('ID', {
            'fields': ['id']
        }),
        ('Name', {
            'fields': ['forename', 'middle_name', 'surname']
        }),
        ('Addresses', {
            'fields': ['addresses'],
        }),
        ('Contact Information', {
            'fields': ['contacts'],
        })
    ]
    inlines = [ContactPhoneAdminInline, ContactEmailAdminInline, AddressAdminInline]


