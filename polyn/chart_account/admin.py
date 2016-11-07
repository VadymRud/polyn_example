from django.contrib import admin
from .models import ChartAccaunt, ChartAccauntGroup, Subconto
from django.utils.translation import ugettext_lazy as _


class ChartAccauntAdmin(admin.ModelAdmin):
    fieldsets = [
            (_('General information'), {'fields': ['number', 'name', 'group', 'date',  'description', 'code', 'subconto',
                'active_passive', 'quantitative']}),
            (_('Active'), {'fields': ['active'], 'classes': ['collapse']}),
        ]
    readonly_fields = ('code',)
    list_display = ('__str__', 'name')


admin.site.register(ChartAccaunt, ChartAccauntAdmin)


class ChartAccauntGroupAdmin(admin.ModelAdmin):
    fieldsets = [
            (_('General information'), {'fields': ['name',  'date', 'number', 'code']}),
            (_('Active'), {'fields': ['active'], 'classes': ['collapse']}),
        ]
    readonly_fields = ('code',)
    list_display = ('__str__', 'name')


admin.site.register(ChartAccauntGroup, ChartAccauntGroupAdmin)

class SubcontoAdmin(admin.ModelAdmin):
    fieldsets = [
            (_('General information'), {'fields': ['name',  'date', 'number', 'code']}),
            (_('Active'), {'fields': ['active'], 'classes': ['collapse']}),
        ]
    readonly_fields = ('code',)
    list_display = ('__str__', 'name')


admin.site.register(Subconto, ChartAccauntGroupAdmin)