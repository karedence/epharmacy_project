from django.conf import settings  # Import the settings module

from django.db import models

class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    pharmacies = models.ManyToManyField(Pharmacy, related_name='medicines')

    def __str__(self):
        return self.name




class SearchLog(models.Model):
    # Use the custom user model referenced by settings.AUTH_USER_MODEL
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE, related_name='search_logs')
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the timestamp when a search is made
    timestamp = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.patient.username if self.patient else 'Anonymous'} searched {self.medicine.name} on {self.created_at}"
