from django.db import models
from django.urls import reverse

class Supplier(models.Model):
    name = models.CharField(max_length=100, default='')
    shipment_postal_code = models.CharField(max_length=100, default='')
    shipment_address = models.CharField(max_length=100, default='')

    def get_absolute_url(self):
        return reverse('supplier-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
