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
    car_number = models.CharField(db_column="car_number", null=False, max_length=20, default="")
    mileage = models.CharField(db_column="mileage", null=False, max_length=20, default="")
    contact  = models.CharField(db_column="contact", null=False, max_length=20)
    location= models.CharField(db_column="location", null=False, max_length=20)
    privacy_agreement = models.BooleanField(db_column = "privacy_agreement", null=False, default=False)
    status_consulting = models.CharField(max_length=20, db_column = "status_consulting", null=False, default='상담중')
    status_selling = models.CharField(max_length=20, db_column = "status_selling", null=False, default='판매예약중')
    created_at = models.DateTimeField(db_column="created_at", null=False, default=timezone.now)
    
    class Meta:
        db_table = "consulting"
        

class Sell(models.Model):
    
    car_name = models.CharField(db_column="car_name", null=False, max_length=20)
    car_number = models.CharField(db_column="car_number", null=False, max_length=20, default="")
    mileage = models.CharField(db_column="mileage", null=False, max_length=20, default="")
    contact  = models.CharField(db_column="contact", null=False, max_length=20)
    location= models.CharField(db_column="location", null=False, max_length=20)
    privacy_agreement = models.BooleanField(db_column = "privacy_agreement", null=False, default=False)
    status_consulting = models.CharField(max_length=20, db_column = "status_consulting", null=False, default='상담중')
    status_selling = models.CharField(max_length=20, db_column = "status_selling", null=False, default='판매예약중')
    created_at = models.DateTimeField(db_column="created_at", null=False, default=timezone.now)
    
    class Meta:
        db_table = "sell"


class Buy(models.Model):
    
    car_name = models.CharField(db_column="car_name", null=False, max_length=20)
    car_number = models.CharField(db_column="car_number", null=False, max_length=20, default="")
    mileage = models.CharField(db_column="mileage", null=False, max_length=20, default="")
    contact  = models.CharField(db_column="contact", null=False, max_length=20)
    location= models.CharField(db_column="location", null=False, max_length=20)
    privacy_agreement = models.BooleanField(db_column = "privacy_agreement", null=False, default=False)
    status_consulting = models.CharField(max_length=20, db_column = "status_consulting", null=False, default='상담중')
    status_selling = models.CharField(max_length=20, db_column = "status_selling", null=False, default='판매예약중')
    created_at = models.DateTimeField(db_column="created_at", null=False, default=timezone.now)
    
    class Meta:
        db_table = "buy"


class Installment(models.Model):
    
    car_name = models.CharField(db_column="car_name", null=False, max_length=20)
    car_number = models.CharField(db_column="car_number", null=False, max_length=20, default="")
    mileage = models.CharField(db_column="mileage", null=False, max_length=20, default="")
    contact  = models.CharField(db_column="contact", null=False, max_length=20)
    location= models.CharField(db_column="location", null=False, max_length=20)
    privacy_agreement = models.BooleanField(db_column = "privacy_agreement", null=False, default=False)
    status_consulting = models.CharField(max_length=20, db_column = "status_consulting", null=False, default='상담중')
    status_selling = models.CharField(max_length=20, db_column = "status_selling", null=False, default='판매예약중')
    created_at = models.DateTimeField(db_column="created_at", null=False, default=timezone.now)
    
    class Meta:
        db_table = "installment"


class Admin(models.Model):

    name = models.CharField(max_length=10, db_column="name")
    password = models.CharField(max_length=20, db_column="password")

    class Meta:
        db_table = "admin"