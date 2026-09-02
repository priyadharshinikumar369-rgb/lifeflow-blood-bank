from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# ===============================
# LOGIN
# ===============================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


# ===============================
# REGISTER
# ===============================

def register_view(request):

    if request.method == "POST":

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # Check empty fields
        if not username or not password or not confirm_password:
            messages.error(request, "Please fill in all fields.")
            return render(request, 'accounts/register.html')

        # Check passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/register.html')

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'accounts/register.html')

        # Create user
        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(
            request,
            "Registration successful! Please login."
        )

        return redirect('login')

    return render(request, 'accounts/register.html')


# ===============================
# LOGOUT
# ===============================

def logout_view(request):

    logout(request)

    messages.success(request, "You have been logged out successfully.")

    return redirect('home')