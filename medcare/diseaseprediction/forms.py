from django import forms

class DiabetesInputForm(forms.Form):
    Pregnancies = forms.IntegerField(
        min_value=0, max_value=20, label="Pregnancies",
        help_text="(0–20 pregnancies)"
    )
    Glucose = forms.FloatField(
        min_value=0, max_value=199, label="Plasma Glucose",
        help_text="(mg/dL)"
    )
    BloodPressure = forms.FloatField(
        min_value=0, max_value=122, label="Blood Pressure",
        help_text="(mm Hg)"
    )
    SkinThickness = forms.FloatField(
        min_value=0, max_value=60, label="Skin Thickness",
        help_text="(mm)"
    )
    Insulin = forms.FloatField(
        min_value=0, max_value=510, label="2-Hour Serum Insulin",
        help_text="(μU/mL)"
    )
    BMI = forms.FloatField(
        min_value=0, max_value=55, label="Body Mass Index (BMI)",
        help_text="(kg/m²)"
    )
    DiabetesPedigreeFunction = forms.FloatField(
        min_value=0.08, max_value=3.5, label="Diabetes Pedigree Function",
        help_text="(0.08–3.5)"
    )
    Age = forms.IntegerField(
        min_value=15, max_value=81, label="Age",
        help_text="(years)"
    )


class AIDsInputForm(forms.Form):
    time = forms.IntegerField(
        min_value=0,
        label="Time (days)",
        help_text="Days since baseline"
    )
    trt = forms.ChoiceField(
        choices=[('0', 'Standard'), ('1', 'Experimental')],
        label="Treatment"
    )
    age = forms.IntegerField(
        min_value=18, max_value=100,
        label="Age (years)",
        help_text="Range: 18-100 years"
    )
    wtkg = forms.FloatField(
        min_value=30, max_value=200,
        label="Weight (kg)",
        help_text="Range: 30-200 kg"
    )
    hemo = forms.FloatField(
        min_value=5, max_value=20,
        label="Hemoglobin (g/dL)",
        help_text="Range: 5-20 g/dL"
    )
    drugs = forms.IntegerField(
        min_value=0, max_value=20,
        label="Number of Drugs",
        help_text="Range: 0-20 drugs"
    )
    karnof = forms.IntegerField(
        min_value=0, max_value=100,
        label="Karnofsky Score",
        help_text="Range: 0-100"
    )
    oprior = forms.ChoiceField(
        choices=[('0', 'No'), ('1', 'Yes')],
        label="Prior Treatment"
    )
    z30 = forms.ChoiceField(
        choices=[('0', 'Negative'), ('1', 'Positive')],
        label="Z30 Status"
    )
    preanti = forms.IntegerField(
        min_value=0,
        label="Pre-anti",
        help_text="Minimum: 0"
    )
    race = forms.ChoiceField(
        choices=[('1', 'White'), ('2', 'Black'), ('3', 'Hispanic'), ('4', 'Asian'), ('5', 'Other')],
        label="Race"
    )
    gender = forms.ChoiceField(
        choices=[('0', 'Male'), ('1', 'Female')],
        label="Gender"
    )
    str2 = forms.ChoiceField(
        choices=[('0', 'No'), ('1', 'Yes')],
        label="STR2"
    )
    strat = forms.IntegerField(
        min_value=1, max_value=3,
        label="Stratum",
        help_text="Range: 1-3"
    )
    symptom = forms.ChoiceField(
        choices=[('0', 'Asymptomatic'), ('1', 'Symptomatic')],
        label="Symptomatic"
    )
    treat = forms.ChoiceField(
        choices=[('0', 'Control'), ('1', 'Treatment')],
        label="Treatment Indicator"
    )
    offrt = forms.ChoiceField(
        choices=[('0', 'No'), ('1', 'Yes')],
        label="Off Treatment"
    )
    cd40 = forms.IntegerField(
        min_value=0,
        label="CD40 Count",
        help_text="Minimum: 0"
    )
    cd420 = forms.IntegerField(
        min_value=0,
        label="CD420 Count",
        help_text="Minimum: 0"
    )
    cd80 = forms.IntegerField(
        min_value=0,
        label="CD80 Count",
        help_text="Minimum: 0"
    )
    cd820 = forms.IntegerField(
        min_value=0,
        label="CD820 Count",
        help_text="Minimum: 0"
    )
