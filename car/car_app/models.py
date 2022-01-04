from django.db import models
import datetime
import os
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.utils.deconstruct import deconstructible
from django.utils import timezone

from django.contrib.auth.models import User



class Consulting(models.Model):
    
    car_name = models.CharField(db_column="car_name", null=False, max_length=20)
    contact  = models.CharField(db_column="contact", null=False, max_length=20)
    location= models.CharField(db_column="location", null=False, max_length=20)
    privacy_agreement = models.BooleanField(db_column = "privacy_agreement", null=False, default=False)
    created_at = models.DateTimeField(db_column="created_at", null=False, default=timezone.now)
    
    class Meta:
        db_table = "consulting"