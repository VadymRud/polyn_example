from django.contrib import admin
from .models import AccountingEntry
from django.utils.translation import ugettext_lazy as _


class AccountingEntryAdmin(admin.ModelAdmin):
    fieldsets = [
            (_('General information'), {'fields': ['date', 'description', 'account_debit', 'account_credit',
                                                   'count_debit', 'count_credit', 'sum_debit', 'sum_credit']}),
            (_('Active'), {'fields': ['active'], 'classes': ['collapse']}),
        ]
    readonly_fields = ('code',)
    list_display = ('__str__', 'sum_debit', 'sum_credit')


admin.site.register(AccountingEntry, AccountingEntryAdmin)