from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    city = models.CharField(max_length=100, blank=True,null=True, verbose_name='City')
    workplace = models.CharField(max_length=100, blank=True,null=True, verbose_name='Workplace')
    date_birth = models.DateField(null=True, blank=True, verbose_name='Date of birth')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone')
    sex = models.CharField(max_length=1, blank=True, null=True, verbose_name="Sex")
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Address')
    family_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='Family status')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, verbose_name='Profile picture')


