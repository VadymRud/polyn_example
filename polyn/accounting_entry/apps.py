from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountingEntryConfig(AppConfig):
    name = 'accounting_entry'
    verbose_name = _('Accounting Entry')
