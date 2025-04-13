from django.urls import path
from homeremedies.views import *
urlpatterns = [
    path('',home_remedies_view, name='home_homeremedies'),
    path('diseases/<int:bodypart_id>/', diseases_view, name='diseases'),
    path('remedies/<int:disease_id>/', remedies_view, name='remedies'),
    path('get_remedies/', get_remedies_view, name='get_remedies'),
]
