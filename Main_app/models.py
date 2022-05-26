from django.db import models


# Create your models here.
class LaborClass(models.Model):
    ACTIVE_STATUS = [('Y', 'Active'),
                     ('N', 'Inactive'),
                     ]

    labor_class = models.CharField(max_length=100, primary_key=True)
    billing_code = models.CharField(max_length=20)
    rates = models.PositiveIntegerField(blank=True)
    active = models.CharField(max_length=1, choices=ACTIVE_STATUS, default='Y')

    objects = models.Manager()

    class Meta:
        db_table = "LaborCode"
