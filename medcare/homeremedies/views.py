from django.shortcuts import render

# Create your views here.
"""def home_homeremedies(request):
    return render(request, 'homeremedies/home_homeremedies.html')
"""
from django.shortcuts import render
from .models import BodyPart, Disease, Remedy
from medcare.decorators import login_required_redirect



import csv
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def load_data():
    data = []
    csv_file_path = r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\data\ram_remedy(1).csv"
    with open(csv_file_path, newline='', encoding='Windows-1252') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def get_remedies_for_prompt(prompt):
    """
    Searches for disease names in the prompt and returns a dictionary
    with diseases as keys and a list of [remedy, remedy_details] pairs as values.
    """
    prompt_lower = prompt.lower()
    remedies_found = {}
    for row in load_data():
        if len(row) < 4:
            continue
        body_part, disease, remedy_name, remedy_details = row
        # Check if the disease is mentioned in the prompt
        if disease.lower() in prompt_lower:
            disease_key = disease.lower()
            if disease_key not in remedies_found:
                remedies_found[disease_key] = [[remedy_name, remedy_details]]
            else:
                remedies_found[disease_key].append([remedy_name, remedy_details])
    return remedies_found

@csrf_exempt
def get_remedies_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "")
            results = get_remedies_for_prompt(prompt)
            return JsonResponse({"results": results}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)






def home_remedies_view(request):
    body_parts = BodyPart.objects.all()
    return render(request, 'homeremedies/home_homeremedies.html', {'body_parts': body_parts})


def diseases_view(request, bodypart_id):
    diseases = Disease.objects.filter(body_part_id=bodypart_id)
    return render(request, 'homeremedies/diseases.html', {'diseases': diseases})


def remedies_view(request, disease_id):
    remedies = Remedy.objects.filter(disease_id=disease_id)
    return render(request, 'homeremedies/remedies.html', {'remedies': remedies})









