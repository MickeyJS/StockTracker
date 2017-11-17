from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^addInstrument$', views.add_new_instrument, name='add_new_instrument'),
    url(r'^allInstruments$', views.show_all_instruments, name='show_all_instruments'),
    url(r'^.*$', views.superuser_panel, name='superuser_panel'),  # main superuser page
]
