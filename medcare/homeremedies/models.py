from django.db import models

class BodyPart(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Disease(models.Model):
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE, related_name="diseases")
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Remedy(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name="remedies")
    name = models.CharField(max_length=200)
    details = models.TextField()

    def __str__(self):
        return self.name
