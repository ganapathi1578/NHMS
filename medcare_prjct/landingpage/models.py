from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed passwords
    dob = models.DateField()
    address = models.TextField()

    def save(self, *args, **kwargs):
        if not is_password_usable(self.password):  # More reliable way to check hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.full_name


class Clinic(models.Model):
    doctor_name = models.CharField(max_length=100)
    clinic_name = models.CharField(max_length=100)
    clinic_email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    clinic_address = models.TextField()

    def save(self, *args, **kwargs):
        if not is_password_usable(self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.clinic_name


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    hospital_email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    hospital_address = models.TextField()
    registration_number = models.CharField(max_length=50, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Standard GPS precision
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not is_password_usable(self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.hospital_name
