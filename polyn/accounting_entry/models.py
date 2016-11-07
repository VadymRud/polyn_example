from django.db import models
import uuid
from decimal import Decimal
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from chart_account.models import ChartAccaunt, Subconto


class MoneyField(models.DecimalField):
    """Base modelfield for money fields"""

    def __init__(self, verbose_name=None, name=None, default=Decimal(0.0), **kwargs):
        kwargs['max_digits'] = 23
        kwargs['decimal_places'] = 8
        kwargs['default'] = default
        super().__init__(verbose_name, name, **kwargs)


class BaseAccountingEntry(models.Model):
    code = models.UUIDField( default=uuid.uuid4, verbose_name=_('Unique code'), editable=False)
    date = models.DateTimeField(default=datetime.now, verbose_name=_('Date creation'))
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    description = models.CharField(max_length=255, verbose_name=_('Full name'))

    account_debit = models.ForeignKey(ChartAccaunt, verbose_name=_('Chart Accaunt Debit'),
                                      related_name='chart_accaunt_debit')
    account_credit = models.ForeignKey(ChartAccaunt, verbose_name=_('Chart Accaunt Debit'),
                                       related_name='chart_accaunt_credit')
    count_debit = models.BigIntegerField(blank=True, null=True, verbose_name=_('Count Debit'))
    count_credit = models.BigIntegerField(blank=True, null=True, verbose_name=_('Count Credit'))
    sum_debit = MoneyField(verbose_name=_('Sum Debit'))
    sum_credit = MoneyField(verbose_name=_('Sum Credit'))

    class Meta:
        abstract = True


class AccountingEntry(BaseAccountingEntry):
    def __str__(self):
        return '%s %s' % (self.account_debit.number, self.account_credit.number)


    class Meta:
        ordering = ['date']
        verbose_name = _('Accounting Entry')
        verbose_name_plural = _('Accounting Entries')