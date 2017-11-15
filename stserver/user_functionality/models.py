from django.db import models
import django

MAX_CHAR_FIELD_LEN = 50
MAX_CHANGE_TYPE_LEN = 10


class User(models.Model):
    name = models.CharField(max_length=MAX_CHAR_FIELD_LEN, blank=True)
    surname = models.CharField(max_length=MAX_CHAR_FIELD_LEN, blank=True)
    email = models.CharField(max_length=MAX_CHAR_FIELD_LEN, blank=True)
    tel_number = models.IntegerField(default=123456789)  # 00 48 123 456 789 - with country code


class SingleSubscription(models.Model):
    """
        User can choose which instruments he want to observe, define rules for this subscription
        and define the time period when he wants to be notified about changes. This class is
        a representation of every such object.
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    instrument_id = models.ForeignKey('superuser_functionality.Instrument')
    date_from = models.DateTimeField(default=django.utils.timezone.now)
    date_to = models.DateTimeField(default=django.utils.timezone.now)
    change_type = models.CharField(max_length=MAX_CHANGE_TYPE_LEN)  # percentage/value...
    change_value = models.FloatField(default=0.0)
