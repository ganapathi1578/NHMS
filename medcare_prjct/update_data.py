import os
import csv
import django
from homeremedies.models import BodyPart, Disease, Remedy
#setup environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medcare.settings")
django.setup()


def load_data():
    with open(r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\data\ram_remedy(1).csv", newline='', encoding='Windows-1252') as file:
        reader = csv.reader(file)
        #next(reader)  # Skip header row

        bodypart_cache = {}
        disease_cache = {}

        remedies = []

        for row in reader:
            body_part_name, disease_name, remedy_name, remedy_details = row

            # Fetch or Create Body Part
            if body_part_name not in bodypart_cache:
                bodypart, _ = BodyPart.objects.get_or_create(name=body_part_name)
                bodypart_cache[body_part_name] = bodypart
            else:
                bodypart = bodypart_cache[body_part_name]

            # Fetch or Create Disease
            if disease_name not in disease_cache:
                disease, _ = Disease.objects.get_or_create(name=disease_name, body_part=bodypart)
                disease_cache[disease_name] = disease
            else:
                disease = disease_cache[disease_name]

            # Add Remedy to list
            remedies.append(Remedy(disease=disease, name=remedy_name, details=remedy_details))

        # Bulk insert Remedies
        Remedy.objects.bulk_create(remedies)
        print("Data loaded successfully!")

# Run function
load_data()
