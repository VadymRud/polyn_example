from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import ProductCatalog

class  ProductCatalogAdmin(admin.ModelAdmin):
    fieldsets = [
            (_('General information'), {'fields': ['number', 'name', 'date', 'parent',  'description']}),
            (_('Active'), {'fields': ['active'], 'classes': ['collapse']}),
        ]
    readonly_fields = ('code',)
    list_display = ('__str__', 'name')


admin.site.register(ProductCatalog, ProductCatalogAdmin)

