from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stock/', include('stock.urls')),
    url(r'^currency/', include('currency.urls')),
    url(r'^', include('currency.urls')),
]
