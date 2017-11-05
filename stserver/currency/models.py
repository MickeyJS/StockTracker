from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=128)

    def __str__(self):
        return '[' + self.code + '] ' + self.name

class Rate(models.Model):
    code = models.ForeignKey(Currency, on_delete=models.CASCADE)
    rate = models.FloatField()
    time = models.DateTimeField()
    zone = models.CharField(max_length=3)

    def __str__(self):
        return '[' + str(self.code.code) + '] ' + str(self.rate) + '\t[' + str(self.time) + ']'