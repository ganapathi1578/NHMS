from django.shortcuts import render, redirect, HttpResponse
from organavailability.forms import OrganDonationForm, OrganSearchForm
from landingpage.models import Hospital  # Import Hospital model
from organavailability.models import Organ
from django.contrib.auth.decorators import login_required
import json
import osmnx as ox
import networkx as nx
from django.shortcuts import render
from django.http import JsonResponse
from organavailability.models import Organ
from landingpage.models import Hospital
from django.shortcuts import render
from organavailability.forms import OrganSearchForm
from organavailability.models import Organ
import osmnx as ox
#from medcare.decorators import login_required_redirect #, allowed_users
from django.contrib.auth.decorators import login_required
from medcare import settings
import os

def find_distance(G, coord1, coord2):
    print("requested for the distance")
    if coord1 and coord2:
        print("valid cordinates")
        node1 = ox.distance.nearest_nodes(G, float(coord1[1]), float(coord1[0]))  # (lon, lat) -> (lat, lon)
        node2 = ox.distance.nearest_nodes(G, float(coord2[1]), float(coord2[0]))
        distance_m = nx.shortest_path_length(G, node1, node2, weight='length')
        print(coord1, coord2, distance_m)
        return distance_m / 1000
    else:
        return 0



def page_searchorgan(request):
    form = OrganSearchForm(request.GET or None)  # Bind form with GET parameters
    organs = Organ.objects.all()
    
    if form.is_valid():
        organ_name = form.cleaned_data.get('organ_name')
        blood_type = form.cleaned_data.get('blood_type')
        
        if organ_name:  # Only filter if a specific organ is chosen
            organs = organs.filter(organ_name__iexact=organ_name)
        if blood_type:  # Only filter if a specific blood type is chosen
            organs = organs.filter(blood_type__iexact=blood_type)

    user_lat = request.GET.get('latitude')
    user_lon = request.GET.get('longitude')
    
    organ_data = []
    # Load your graph for distance calculations (adjust the path as needed)
    graph_path = os.path.join(settings.BASE_DIR, 'mapthings', 'mizoram_graph.graphml')
    G = ox.load_graphml(graph_path)


    # Taking mzus location
    user_lat = 23.7349213
    user_lon = 92.62665429
    if user_lat and user_lon:
        user_location = (float(user_lat), float(user_lon))

        for organ in organs:
            hospital_location = (organ.hospital.latitude, organ.hospital.longitude)
            distance = find_distance(G, user_location, hospital_location)

            organ_data.append({
                "organ_id": organ.organ_id,
                "organ_name": organ.organ_name,
                "donor_age": organ.age,
                "blood_type": organ.blood_type,
                "donation_date": organ.date_of_donation,
                "sex": organ.sex,
                "hospital_name": organ.hospital.hospital_name,  # assuming Hospital has a name field
                "hospital_email": organ.hospital.hospital_email,  # assuming Hospital has an email field
                "distance": round(distance, 3)
            })

        organ_data.sort(key=lambda x: x["distance"])
    else:
        # If no user location provided, just convert queryset to list of dicts (without distance)
        for organ in organs:
            organ_data.append({
                "organ_id": organ.organ_id,
                "organ_name": organ.organ_name,
                "donor_age": organ.age,
                "blood_type": organ.blood_type,
                "donation_date": organ.date_of_donation,
                "sex": organ.sex,
                "hospital_name": organ.hospital.hospital_name,
                "hospital_email": organ.hospital.hospital_email,
                "distance": None
            })

    return render(request, 'organavailability/o3rgansearh.html', {"form": form, "organs": organ_data})





def home_organavailability(request):
    return render(request, 'organavailability/home_organavailability.html')


def donate_organ(request):
    if request.method == "POST":
        form = OrganDonationForm(request.POST)
        if form.is_valid():
            organ = form.save(commit=False)
            organ.save()
            return HttpResponse('Organ added successfully')
    else:
        form = OrganDonationForm()

    return render(request, 'donate_organ.html', {'form': form})


