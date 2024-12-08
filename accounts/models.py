
from django.conf import settings  # Import the settings module
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
