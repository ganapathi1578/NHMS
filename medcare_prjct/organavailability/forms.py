from django import forms
from organavailability.models import Organ
from landingpage.models import Hospital

class OrganDonationForm(forms.ModelForm):
    hospital = forms.ModelChoiceField(
        queryset=Hospital.objects.all(),  # Show all hospitals in dropdown
        empty_label="Select a Hospital",  # Placeholder text
        required=True
    )

    class Meta:
        model = Organ
        fields = ['organ_name', 'blood_type', 'age', 'sex', 'hospital']

class OrganSearchForm(forms.Form):
    organ_name = forms.ChoiceField(
        choices=[('', 'All Organs')] + [(org, org) for org in Organ.objects.values_list("organ_name", flat=True).distinct()],
        required=False
    )
    
    blood_type = forms.ChoiceField(
        choices=[('', 'All Blood Types')] + [(b, b) for b in Organ.objects.values_list("blood_type", flat=True).distinct()],
        required=False
    )
