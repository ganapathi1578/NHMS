from django.urls import path
from organavailability.views import *

urlpatterns = [
    path('', home_organavailability, name="home_organavailability"),
    path('searchorgans/', page_searchorgan , name="page_searchorgan"),
    path('addorgans/', donate_organ , name="page_addorgan"),
]
