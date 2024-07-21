from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile
from django.db import IntegrityError

def register(request):
    # I start by checking if the request method is POST, which means the user is submitting the registration form.
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # I create an instance of UserRegisterForm with the submitted data.

        if form.is_valid():
            # I check if the form is valid.

            user = form.save()
            try:
                # Ensure a profile is created only if it doesn't already exist
                Profile.objects.get_or_create(user=user)
            except IntegrityError:
                # Handle the case where the profile already exists
                return redirect('home')
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        # If the request method is not POST, I create a blank registration form.
        form = UserRegisterForm()

    # I render the registration template with the form.
    return render(request, 'users/register.html', {'form': form})

@login_required
# I use the login_required decorator to ensure only logged-in users can access the profile view.

def profile(request):
    # Ensure the user has a profile
    try:
        profile = request.user.profile
        # I try to access the user's profile.
    except Profile.DoesNotExist:
        # If the profile does not exist, I redirect the user to the home page.
        return redirect('home')

    if request.method == 'POST':
        # If the request method is POST, it means the user is submitting the profile update form.

        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        # I create an instance of ProfileUpdateForm with the submitted data and files, and the user's profile.

        if p_form.is_valid():
            # I check if the form is valid.
            p_form.save()
            # I save the form data to update the profile.
            return redirect('users:profile')
            # I redirect the user back to the profile page.
    else:
        # If the request method is not POST, I create a form pre-filled with the user's profile data.
        p_form = ProfileUpdateForm(instance=profile)

    # I render the profile template with the form.
    return render(request, 'users/profile.html', {'p_form': p_form})

@login_required
# I use the login_required decorator to ensure only logged-in users can access the enhanced profile view.

def enhanced_profile(request):
    # I try to access the user's profile.
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # If the profile does not exist, I create one for the user.
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        # If the request method is POST, it means the user is submitting the profile update form.

        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        # I create an instance of ProfileUpdateForm with the submitted data and files, and the user's profile.

        if p_form.is_valid():
            # I check if the form is valid.
            p_form.save()
            # I save the form data to update the profile.
            return redirect('users:enhanced_profile')
            # I redirect the user back to the enhanced profile page.
    else:
        # If the request method is not POST, I create a form pre-filled with the user's profile data.
        p_form = ProfileUpdateForm(instance=profile)

    # I render the enhanced profile template with the form.
    return render(request, 'users/enhanced_profile.html', {'p_form': p_form})
