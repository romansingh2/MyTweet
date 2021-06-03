from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import random
from django.contrib.auth import get_user_model
from django.db.models import Q


#User = settings.AUTH_USER_MODEL #reference built in django feature


from django.contrib.auth import get_user_model

class User(AbstractUser):
    pass


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) #Note that the current date is always used; it’s not just a default value that you can override. So even if you set a value for this field when creating the object, it will be ignored. If you want to be able to modify this field, set the following instead of auto_now_add=True:

class PostQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users_id = []
        if profiles_exist:
            followed_users_id = user.following.values_list("user__id", flat=True) #[x.user.id for x in profiles]
        return self.filter(
            Q(user__id__in=followed_users_id) | 
            Q(user=user)
            ).distinct().order_by("-timestamp") #Model.objects

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)

class Post(models.Model):
    # Maps to SQL data
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL) #self represents the same model you are working on
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts") #many users can have many posts, use foreignkey so one user can own many tweets. the on_Delete=cascade means if user is deleted all their posts are deleted too
    likes = models.ManyToManyField(User, related_name='post_user', blank=True, through=PostLike) #through is used to add more data in a ManyToManyField, ie timestamps for when a user likes a post
    tweet = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = PostManager()
    # def __str__(self):
    #     return self.content

    class Meta:
        ordering = ['-id']

    @property 
    def is_retweet(self):
        return self.parents != None
    
    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
