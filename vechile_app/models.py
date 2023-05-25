from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_superuse = models.BooleanField('Is superuse', default=False)
    is_use = models.BooleanField('Is use', default=False)
    is_adim = models.BooleanField('Is adim', default=False)
    
    
class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('1', 'Two Wheelers'),
        ('2', 'Three Wheelers'),
        ('3', 'Four Wheelers'),
    )
    
    alphanumeric_validator = RegexValidator(
        r'^[0-9a-zA-Z]+$',
        'Only alphanumeric characters are allowed.'
    )
    
    vehicle_number = models.CharField(max_length=20, unique=True, validators=[alphanumeric_validator],null=True)
    vehicle_type = models.CharField(max_length=1, choices=VEHICLE_TYPES,null=True)
    vehicle_model = models.CharField(max_length=100,null=True)
    vehicle_description = models.TextField(null=True)