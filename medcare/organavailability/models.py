import random
from django.db import models
from landingpage.models import Hospital
from django import forms





class Organ(models.Model):
    ORGAN_CHOICES = [
        ('Heart', 'Heart'),
        ('Kidney', 'Kidney'),
        ('Liver', 'Liver'),
        ('Lungs', 'Lungs'),
        ('Pancreas', 'Pancreas'),
        ('Intestine', 'Intestine'),
    ]

    BLOOD_TYPES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    organ_id = models.CharField(max_length=8, unique=True, editable=False)
    organ_name = models.CharField(max_length=20, choices=ORGAN_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    age = models.PositiveIntegerField()
    date_of_donation = models.DateField(auto_now_add=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    # Store both hospital name and email
    hospital = models.ForeignKey(Hospital, to_field='hospital_email', on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=255, default='defaulthospital')  # Store hospital name
    hospital_email = models.EmailField(default='default@example.com')  # Store hospital email separately

    def save(self, *args, **kwargs):
        if not self.organ_id:
            self.organ_id = self.generate_organ_id()

        # Auto-fill hospital name and email from the selected Hospital instance
        if self.hospital:
            self.hospital_name = self.hospital.hospital_name
            self.hospital_email = self.hospital.hospital_email

        super().save(*args, **kwargs)

    @staticmethod
    def generate_organ_id():
        return str(random.randint(10000000, 99999999))  # Generates a random 8-digit ID

    def __str__(self):
        return f"{self.organ_name} - {self.organ_id} ({self.hospital_name})"




