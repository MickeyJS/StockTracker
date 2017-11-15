from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^superuser/', include('superuser_functionality.urls')),
    url(r'user/', include('user_functionality.urls')),
    url(r'.*', include('user_functionality.urls')),
]
