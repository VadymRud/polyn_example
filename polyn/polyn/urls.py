from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^rosetta/', include('rosetta.urls')),

]
