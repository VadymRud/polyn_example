from django.db import models
import uuid
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from jsonfield import JSONField


class BaseProduct(models.Model):
    code = models.UUIDField(default=uuid.uuid4, verbose_name = _('Unique code'), editable=False)
    date = models.DateTimeField(default=datetime.now, verbose_name = _('Date creation'))
    active = models.BooleanField(verbose_name = _('Active'), default=True)
    name = models.CharField(max_length=255, verbose_name = _('Full name'))
    number = models.CharField(max_length=255, verbose_name = _('Number'))
    description = models.CharField(max_length=255, verbose_name = _('Description'))

    class Meta:
       abstract = True


class ProductCatalog(BaseProduct, MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name = _('Parent Catalog'))

    def __str__(self):
        return '%s %s' % (self.number, self.name)

    class Meta:
        ordering = ['number']
        verbose_name = _('Product Catalog')
        verbose_name_plural = _('Products Catalogs')


class UnitsOfMeasurement(models.Model):
    code = models.UUIDField(default=uuid.uuid4, verbose_name=_('Unique code'), editable=False)
    name = models.CharField(max_length=255, verbose_name=_('Full name'))
    short_name = models.CharField(max_length=255, verbose_name=_('Short name'))
    value = models.CharField(max_length=255, verbose_name=_('Value'))

    def __str__(self):
        return '%s %s' % (self.short_name, self.name)

    class Meta:
        ordering = ['short_name']
        verbose_name = _('Units of measurement')
        verbose_name_plural = _('Units of measurements')


class Product(BaseProduct):
    catalog = models.ForeignKey(ProductCatalog, null=True, blank=True, verbose_name=_('Catalog'))
    units = models.ForeignKey(UnitsOfMeasurement, null=True, blank=True, verbose_name=_('Units'))
    size = JSONField(null=True, blank=True, verbose_name=_('Units'))

    def __str__(self):
        return '%s %s' % (self.number, self.name)

    class Meta:
        ordering = ['number']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

