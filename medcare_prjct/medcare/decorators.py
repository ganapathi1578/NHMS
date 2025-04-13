from django.http import HttpResponseForbidden
from django.shortcuts import redirect

"""def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated and hasattr(request.user, 'profile') and request.user.profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to view this page.")
        return wrapper_func
    return decorator"""

def login_required_redirect(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Debugging
        print(f"🔍 Session Email: {request.session.get('user_email')}")  
        
        # Check if user session exists
        if not request.session.get('user_email'):  
            return redirect('login')  # Redirect to login page
        
        return view_func(request, *args, **kwargs)
    
    return wrapper_func
