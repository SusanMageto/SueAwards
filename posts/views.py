from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout 
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from projects.models import *
from  .forms import *
from django.contrib import messages

def signup(request):
    # redirect a user to the home page if he is already logged in
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # display a nice message when a new user is registered
            messages.success(request, "Congratulations, you are now a registered user!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # We check if the data is correct
            user = authenticate(email=email, password=password)
            if user:  # If the returned object is not None
                login(request, user)
                  # we connect the user
                messages.success(request,"Login was successful")
                return redirect('home')
            else:  # otherwise an error will be displayed
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def log_out(request):
    logout(request)
    messages.success(request,"logout was successful")
    return redirect(reverse('home'))




@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    projects = Project.objects.filter(user=user).order_by('-id')
    context={
        'profile': profile,
        'user': user,
        'projects':projects,
        }
    return render(request, 'profile.html', context)    


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.user.username, request.POST, request.FILES)
        if form.is_valid():
            bio = form.cleaned_data["bio"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]

            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.bio = bio
            if image:
                profile.image = image
            profile.save()
            messages.success(request,"Profile was updated successfully")
            return redirect("profile", username=user.username)
    else:
        form = EditProfileForm(request.user.username)
    return render(request, "edit_profile.html", {'form': form})


 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from projects.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response



@api_view(['GET'])
def profileList(request):
    profiles = Profile.objects.all()
    # projects = Project.objects.filter(user=profiles.user)
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)  



    