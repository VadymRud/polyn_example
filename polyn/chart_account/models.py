#chart_account
from django.db import models
import uuid
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class BaseChartAccaunt(models.Model):
    code = models.UUIDField( default=uuid.uuid4, verbose_name=_('Unique code'), editable=False)
    date = models.DateTimeField(default=datetime.now, verbose_name=_('Date creation'))
    active = models.BooleanField(verbose_name = _('Active'), default=True)
    name = models.CharField(max_length=255, verbose_name=_('Full name'))
    number = models.CharField(max_length=255, verbose_name=_('Number'))

    class Meta:
       abstract = True


# class Through(BaseChartAccaunt):
#     pass
#     #some = models.CharField(max_length=100, verbose_name = 'Полное имя')

class ChartAccauntGroup(BaseChartAccaunt):
    def __str__(self):
        return '%s %s' % (self.number, self.name)

    class Meta:
        ordering = ['number']
        verbose_name_plural = _('Group Accaunt Plural')


class Subconto(BaseChartAccaunt):
    def __str__(self):
        return '%s %s' % (self.number, self.name)

    class Meta:
        ordering = ['number']
        verbose_name = _('Subconto')
        verbose_name_plural = _('Subconto')



quantitative_choise = (
    (0, _('No')),
    (1, _('quantitative')),
    (2, _('monetary')),
)

active_passive_choises = (
    (1, _('active')),
    (2, _('passive')),
    (3, _('active_passive')),
)

class ChartAccaunt(BaseChartAccaunt):
    group = models.ForeignKey(ChartAccauntGroup, related_name='group', verbose_name = _('Group Accaunt'), null=True)
    description = models.TextField( null=True,  verbose_name = _('Description'))
    quantitative = models.SmallIntegerField( null=True, verbose_name=_('quantitative'), choices=quantitative_choise)
    subconto = models.ManyToManyField(Subconto, related_name='subconto')
    active_passive = models.SmallIntegerField(choices=active_passive_choises, verbose_name=_('Active or Passive'))
    def __str__(self):
        return '%s %s' % (self.number, self.name)

    class Meta:
        ordering = ['number']
        verbose_name_plural = _('Chart Accaunt Plural')
