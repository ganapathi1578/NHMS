from django.contrib import admin
from landingpage.models import User, Clinic, Hospital

# Register your models here.
from django.contrib import admin
from landingpage.models import User, Clinic, Hospital

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'dob', 'address', 'password',)
    search_fields = ('full_name', 'email')
    list_filter = ('dob',)

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('clinic_name', 'doctor_name', 'clinic_email', 'clinic_address','password')
    search_fields = ('clinic_name', 'doctor_name', 'clinic_email')
    list_filter = ('clinic_name',)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital_name', 'hospital_email', 'registration_number', 'hospital_address','latitude', 'longitude')
    search_fields = ('hospital_name', 'hospital_email', 'registration_number')
    list_filter = ('hospital_name',)



