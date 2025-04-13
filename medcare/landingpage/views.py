# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from landingpage.forms import UserSignupForm, ClinicSignupForm, HospitalSignupForm
from landingpage.models import User, Clinic, Hospital
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from landingpage.forms import UserSignupForm, ClinicSignupForm, HospitalSignupForm, LoginForm
from landingpage.models import User, Clinic, Hospital
from medcare.decorators import login_required_redirect


@login_required_redirect
def profile_view(request):
    user_email = request.session.get('user_email')
    
    if not user_email:
        return redirect('login')  # Redirect to login if user is not logged in
    
    user = User.objects.filter(email=user_email).first()
    
    return render(request, 'profile.html', {'user': user})

# Login View
def login_view(request):
    next_url = request.GET.get('home')  # Get 'next' parameter or default to home

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']    

            user = None
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
            elif Clinic.objects.filter(clinic_email=email).exists():
                user = Clinic.objects.get(clinic_email=email)
            elif Hospital.objects.filter(hospital_email=email).exists():
                user = Hospital.objects.get(hospital_email=email)

            if user and check_password(password, user.password):
                request.session['user_email'] = email
                messages.success(request, f"{email} logged in successfully.")
                
                # Redirect to the intended page after login
                return redirect('home')

            messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'title': 'Login'})

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

# Choose Account View
def choose_account(request):
    return render(request, 'choose_account.html')

# User Signup View
def user_signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  # Hash password
            user.save()
            request.session['user_email'] = user.email
            messages.success(request, f"{user.email} logged in successfully.")
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form, 'title': 'User Signup'})

# Clinic Signup View
def clinic_signup(request):
    if request.method == "POST":
        form = ClinicSignupForm(request.POST)
        if form.is_valid():
            clinic = form.save(commit=False)
            clinic.password = make_password(form.cleaned_data['password'])
            clinic.save()
            request.session['user_email'] = clinic.clinic_email
            messages.success(request, f"{clinic.clinic_email} logged in successfully.")
            return redirect('home')
    else:
        form = ClinicSignupForm()
    return render(request, 'signup.html', {'form': form, 'title': 'Clinic Signup'})

# Hospital Signup View
def hospital_signup(request):
    if request.method == "POST":
        form = HospitalSignupForm(request.POST)
        if form.is_valid():
            hospital = form.save(commit=False)
            hospital.password = make_password(form.cleaned_data['password'])
            
            # Capture latitude and longitude from the POST request
            hospital.latitude = request.POST.get("latitude")
            hospital.longitude = request.POST.get("longitude")

            hospital.save()

            request.session['user_email'] = hospital.hospital_email
            messages.success(request, f"{hospital.hospital_email} logged in successfully.")
            return redirect('home')
    else:
        form = HospitalSignupForm()
    return render(request, 'signup.html', {'form': form, 'title': 'Hospital Signup'})


def home(request):
    return render(request, "home.html")
def services(request):
    return render(request, "services.html")
def about(request):
    return render(request, "aboutUs.html")