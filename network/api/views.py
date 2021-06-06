from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from ..forms import PostForm 
from django.utils.http import is_safe_url
from django.conf import settings
import random
from ..models import User, Post
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import PostSerializer, PostActionSerializer, PostCreateSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
User = get_user_model()

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


@api_view(['POST']) #http method the client == POST.  Takes a list of HTTP methods that your view should respond to.
# @authentication_classes([SessionAuthentication, MyCustomAuth])
@permission_classes([IsAuthenticated]) #Rest API course 
def post_create_view(request, *args, **kwargs): 
    print(request.data)
    serializer = PostCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status = 201)
    return Response({}, status=400)

@api_view(['GET'])
def post_detail_view(request, post_id, *args, **kwargs):
    qs = Post.objects.filter(id=post_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = PostSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated]) 
def post_delete_view(request, post_id, *args, **kwargs):
    qs = Post.objects.filter(id=post_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message: You cannot delete this post"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message: Post removed"}, status=200)




def get_paginated_queryset_response(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = PostSerializer(paginated_qs, many=True)
    return paginator.get_paginated_response(serializer.data) # Response( serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_feed_view(request, *args, **kwargs):
    user = request.user
    qs = Post.objects.feed(user)
    return get_paginated_queryset_response(qs, request) 

@api_view(['GET'])
def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    username = request.GET.get('username') #url will pass in something like username = romansingh2
    if username != None:
        qs = qs.filter(user__username__iexact=username)
    return get_paginated_queryset_response(qs, request)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_action_view(request, *args, **kwargs):
    '''
    id is required.
    Action options are: like, unlike, retweet
    '''
    serializer = PostActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        Post_id = data.get("id")
        action = data.get("action")
        tweet = data.get("tweet")
        qs = Post.objects.filter(id=Post_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = PostSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = PostSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "retweet":
            new_Post = Post.objects.create(
                user=request.user,
                parent=obj,
                tweet=tweet,
            )
            serializer = PostSerializer(new_Post)
            return Response(serializer.data, status=201)
    return Response({}, status=200)
            

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
"""
def post_create_view_pure_django(request, *args, **kwargs):

    '''
    REST API Create View -> DRF
    '''
    user = request.user
    if not request.user.is_authenticated:    #if user not in database
        user = None 
        if request.is_ajax():                                                   #AJAX just uses a combination of: A browser built-in XMLHttpRequest object (to request data from a web server)JavaScript and HTML DOM (to display or use the data)
            return JsonResponse({}, status = 401)    
        return redirect("login")  #if user not found in database and the request is ajax, send them back to login 
    form = PostForm(request.POST or None)   #use forms to submite data
    next_url = request.POST.get("next") or None  
    if form.is_valid():
        obj = form.save(commit=False) 
        obj.user = user
        #do other form related logic
        obj.save() 
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201) # 201 == created items
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = PostForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'network/form.html', context = {"form": form})


def post_list_view_pure_django(request, *args, **kwargs):
    
    #REST API VIEW
    #Consume by JavaScript or Swift/Java/iOS/Andriod
    #return json data
    
    qs = Post.objects.all() #qs is equal to all the data in the post class
    Posts_list = [x.serialize() for x in qs]  
    data = {
        "isUser": False,
        "response": Posts_list
    }
    return JsonResponse(data)


def post_detail_view_pure_django(request, Post_id, *args, **kwargs):
    
    #REST API VIEW
    #Consume by JavaScript or Swift/Java/iOS/Andriod
    #return json data
    
    data = { "id": Post_id,}
    status = 200
    try: 
        obj = Post.objects.get(id=Post_id)
        data['tweet'] = obj.tweet
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
    

""" 




