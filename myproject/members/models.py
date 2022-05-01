from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Patient(User):
    birthday = models.DateField('%Y-%m-%d')
    phone_number = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("patient")
        verbose_name_plural = _("patients")
        #abstract = True
    
        def __str__(self):
            return self.username

    def age(self):
        import datetime
        return int(datetime.date.today() - self.birthday).days / 365.25  


class Specialties(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Doctor(User):
    spcialty = models.ForeignKey(Specialties, on_delete = models.CASCADE)

    class Meta:
        verbose_name = _("doctor")
        verbose_name_plural = _("doctors")
        #abstract = True

        def __str__(self):
            return self.username

