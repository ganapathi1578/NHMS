from django.urls import path
from landingpage.views import choose_account, user_signup, clinic_signup, hospital_signup, login_view, logout_view, home, services, about, profile_view

urlpatterns = [
    path("", home, name="home"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('choose-account/', choose_account, name='choose_account'),
    path('signup/user/', user_signup, name='user_signup'),
    path('signup/clinic/', clinic_signup, name='clinic_signup'),
    path('signup/hospital/', hospital_signup, name='hospital_signup'),
    path('services/', services, name='services'),
    path('aboutus/', about, name='aboutUs'),
    path('profile/', profile_view, name='profile'),

    
]