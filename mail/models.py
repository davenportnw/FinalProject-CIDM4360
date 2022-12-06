from django.db import models

# Create your models here.


STATUS_CHOICES = (
    ("DELIVERED", "delivered"),
    ("PENDING", "pending"),
    ("UNKNOWN", "unknown")
)


class Package(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    posting_service = models.CharField(max_length=50)
    received = models.DateTimeField('Date office received')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True)
    owner = models.ForeignKey('Resident', models.SET_NULL, blank=True, null=True)


class Resident(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    unit_number = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + str(self.unit_number)
