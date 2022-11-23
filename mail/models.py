from django.db import models


# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    posting_service = models.CharField(max_length=50)
    received = models.DateTimeField('Date office received')


class Resident(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    unit_number = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + str(self.unit_number)
