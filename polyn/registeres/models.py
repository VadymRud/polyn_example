from django.db import models
import uuid
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class BaseRegisteres(models.Model):
    code = models.UUIDField( default=uuid.uuid4, verbose_name = _('Unique code'), editable=False)
    date = models.DateTimeField(default=datetime.now, verbose_name = _('Date creation'))
    active = models.BooleanField(verbose_name = _('Active'), default=True)
    name = models.CharField(max_length=255, verbose_name = _('Full name'))
    number = models.CharField(max_length=255, verbose_name = _('Number'))

    class Meta:
       abstract = True



class Stock(BaseRegisteres):
    pass
