from django.test import TestCase
from .models import Post, User, PostLike
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


# Create your tests here.
User = get_user_model()

class PostTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='cfe', password='somepassword')
        self.userb = User.objects.create_user(username='cfe-2', password='somepassword2')
        Post.objects.create(tweet="my tweet", user=self.user)
        Post.objects.create(tweet="my tweet", user=self.user)
        Post.objects.create(tweet="my tweet", user=self.userb)
        self.currentCount = Post.objects.all().count() #total number of posts
    
    def test_post_created(self):
        Post_obj = Post.objects.create(tweet="my second tweet", user=self.user)
        self.assertEqual(Post_obj.id, 4)
        self.assertEqual(Post_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client
    
    def test_post_list(self):
        client = self.get_client()
        response = client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        #print(response.json())
    
    def test_posts_related_name(self):
        user = self.user
        self.assertEqual(user.posts.count(), 2)


    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/posts/action/", {"id": 1, "action": "like"})
        like_count = response.json().get("likes")
        user = self.user
        my_like_instances_count = response.json().get("likes")
        my_related_likes = user.post_user.count()
        my_like_instances = user.postlike_set.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(like_count, 1)
        self.assertEqual(my_like_instances_count, 1)
        self.assertEqual(my_like_instances_count, my_related_likes)

    def test_action_unlike(self):
        client = self.get_client() #The test client is a Python class that acts as a dummy Web browser, allowing you to test your views and interact with your Django-powered application programmatically.
        response = client.post("/api/posts/action/", {"id": 2, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/posts/action/", {"id": 2, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)
    
    def test_action_retweet(self):
        client = self.get_client()
        response = client.post("/api/posts/action/", {"id": 2, "action": "retweet"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_Post_id = data.get("id")
        self.assertNotEqual(2, new_Post_id) #the new post should not have the same id as the original post
        self.assertEqual(self.currentCount + 1, new_Post_id)

    def test_post_create_api_view(self):
        request_data = {"tweet": "This is my test tweet"}
        client = self.get_client()
        response = client.post("/api/posts/create/", request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_Post_id = response_data.get("id")
        self.assertEqual(self.currentCount + 1, new_Post_id)

    def test_post_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/posts/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)

    def test_post_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/api/posts/1/delete/")
        self.assertEqual(response.status_code, 200)
        client = self.get_client()
        response = client.delete("/api/posts/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/api/posts/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)        
 