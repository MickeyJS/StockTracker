from django.db import models
import django

MAX_CHAR_FIELD_LEN = 50
MAX_CHANGE_TYPE_LEN = 10


class User(models.Model):
    name = models.CharField(max_length=MAX_CHAR_FIELD_LEN, blank=True)
    surname = models.CharField(max_length=MAX_CHAR_FIELD_LEN, blank=True)
    email = models.CharField(max_length=MAX_CHAR_FIELD_LEN, blank=True)
    tel_number = models.IntegerField(default=123456789)  # 123 456 789

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = self._cut_string_for_char_field(new_name)

    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname):
        self._cut_string_for_char_field(new_surname)

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        if self._email_is_valid(new_email):
            self.email = self._cut_string_for_char_field(new_email)

    def get_tel_number(self):
        return self.tel_number

    def set_tel_number(self, number):
        if self._tel_number_is_valid(number):
            self.tel_number = int(number)

    def _email_is_valid(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False

    def _cut_string_for_char_field(self, string):
        return str(string)[:MAX_CHAR_FIELD_LEN]

    def _tel_number_is_valid(self, number):
        if re.match(r"[0-9]{9}", number):
            return True
        else:
            return False

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.surname, self.email, str(self.tel_number))


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

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.user_id, self.instrument_id, self.change_type, self.change_value,
                                          self.date_from, self.date_to)
