from django import forms
from landingpage.models import User, Clinic, Hospital

# User Signup Form
class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'dob', 'address']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter your address'}),
        }

# Clinic Signup Form
class ClinicSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = Clinic
        fields = ['doctor_name', 'clinic_name', 'clinic_email', 'password', 'clinic_address']
        widgets = {
            'doctor_name': forms.TextInput(attrs={'placeholder': 'Enter doctor\'s name'}),
            'clinic_name': forms.TextInput(attrs={'placeholder': 'Enter clinic name'}),
            'clinic_email': forms.EmailInput(attrs={'placeholder': 'Enter clinic email'}),
            'clinic_address': forms.Textarea(attrs={'placeholder': 'Enter clinic address'}),
        }

# Hospital Signup Form
class HospitalSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    latitude = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    longitude = forms.DecimalField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Hospital
        fields = ['hospital_name', 'hospital_email', 'password', 'hospital_address', 'registration_number', 'latitude', 'longitude']
        widgets = {
            'hospital_name': forms.TextInput(attrs={'placeholder': 'Enter hospital name'}),
            'hospital_email': forms.EmailInput(attrs={'placeholder': 'Enter hospital email'}),
            'hospital_address': forms.Textarea(attrs={'placeholder': 'Enter hospital address'}),
            'registration_number': forms.TextInput(attrs={'placeholder': 'Enter registration number'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))