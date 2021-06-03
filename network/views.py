from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from .forms import PostForm 
from django.utils.http import is_safe_url
from django.conf import settings
import random
from .models import User, Post, PostLike
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, PostActionSerializer, PostCreateSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model



ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, "network/feed.html")

def posts_list_view(request, *args, **kwargs): #home page
    return render(request, "posts/list.html") 

def posts_detail_view(request, post_id, *args, **kwargs): #home page
    return render(request, "posts/detail.html", context = {"post_id" : post_id})

"""
def login_view(request): 
    if request.method == "POST": 

        # Attempt to sign user in
        username = request.POST["username"]  
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user   
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

"""









