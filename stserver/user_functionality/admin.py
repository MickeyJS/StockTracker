from django.contrib import admin

from .models import User, SingleSubscription

admin.site.register(User)
admin.site.register(SingleSubscription)
