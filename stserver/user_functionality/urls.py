from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^allInstruments', views.show_all_instruments, name='show_all_instruments'),
    url(r'^myInstruments', views.show_user_instruments, name='show_user_instruments'),
    url(r'^editAccount', views.change_user_data, name='change_user_data'),
    url(r'^createAccount', views.create_account, name='create_account'),
    url(r'.*', views.login_user, name='login_user'),  # all endpoints not listed above will redirect to login page
]